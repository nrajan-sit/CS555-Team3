# Import collection package
from collections import namedtuple

# Import parameter package
import sys

# Import datetime package
from datetime import datetime
import datetime as dt
from datetime import date

import pandas as pd
import numpy as np

from gedcom import *


def us10_Marriage_before_14(individuals, families):

    return_flag = True
    error_type = "US10"

    for i in range(len(families)):
        married_date = families.iloc[[i]]['Married'].values[0]
        h_id = families.iloc[[i]]['Husband ID'].values[0]
        w_id = families.iloc[[i]]['Wife ID'].values[0]

        if (individuals.loc[individuals['ID'] == h_id]['Birthday'].values[0]) - married_date <= dt.timedelta(14*365):
            name = individuals.loc[individuals['ID'] ==
                                   h_id]['Name'].values[0].replace('/', '')
            er_message = 'Error {}: Marriage date of {} ({}) occurs before 14 years of Birth'.format(
                error_type, name, h_id)
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                f.write(er_message)
                f.write('\n')
                f.close()

            return_flag = False

        if (individuals.loc[individuals['ID'] == w_id]['Birthday'].values[0]) - married_date <= dt.timedelta(14*365.25):
            name = individuals.loc[individuals['ID'] ==
                                   w_id]['Name'].values[0].replace('/', '')
            er_message = 'Error {}: Marriage date of {} ({}) occurs before 14 years of Birth'.format(
                error_type, name, w_id)
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                f.write(er_message)
                f.write('\n')
                f.close()
            return_flag = False

    return return_flag


def us14_Multiple_Births(individuals, families):

    return_flag = True
    error_type = "US14"

    more_than_5_children = individuals['Child'].replace(
        'NA', pd.NA).dropna().value_counts() > 5
    famlies_with_5_children = more_than_5_children.index[more_than_5_children.values]

    for i in famlies_with_5_children:
        if any(individuals[individuals['Child'] == i]['Birthday'].value_counts() > 5):
            er_message = 'Error {}: Family ({}) has more than five children born at the same time '.format(
                error_type, i.lstrip("{'").rstrip("'}"))
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                f.write(er_message)
                f.write('\n')
                f.close()

            return_flag = False

    return return_flag

#US15 Fewer than 15 siblings: There should be fewer than 15 siblings in a family


def us15_fewer_than_15_siblings(Family):
    eval = True

    for i in Family:
        children_id = i[5].split()
        family_id = i[0]
        #print(children_id)
        count = 0

        for c in children_id:
            count += 1

        if (count >= 15):
            error = 'Error US15: Family (' + \
                family_id + ') has 15 or more siblings.'
            print(error)
            eval = False
            with open('gedcom_output.txt', 'a') as f:
                f.write(error)
                f.write('\n')
                f.close()

    return eval

#US13 Sibling spacing: Birth dates of siblings should be more than 8 months
#apart or less than 2 days apart (twins may be born one day apart,
#e.g. 11:59 PM and 12:02 AM the following calendar day)


def us13_sibling_spacing(Individual, Family):
    eval = True
    #sibling_1_birthday ='#'
    #sibling_2_birthday =''

    for i in Family:
        children_id = i[5].split()

        c = children_id[0]

        for k in Individual:
            if(c == k[0]):
                sibling_1_birthday = k[3]
                sibling_1_name = k[1].replace('/', "")
                sibling_1_id = k[0]

        for d in children_id:
            for l in Individual:
                if(c != d):
                    if(d == l[0]):
                        sibling_2_birthday = l[3]
                        sibling_2_name = l[1].replace('/', "")
                        sibling_2_id = l[0]

                        dif = abs((sibling_1_birthday.year-sibling_2_birthday.year)
                                  * 12 + (sibling_1_birthday.month - sibling_2_birthday.month))
                        dif2 = abs(
                            (sibling_1_birthday-sibling_2_birthday).days)

                        #print(dif2)

                        if((dif < 8) and (dif2 > 2)):

                            error = ('Error US13: Birthdays of siblings '+sibling_1_name+' ('+sibling_1_id+') and ' +
                                     sibling_2_name+' ('+sibling_2_id+') are between 2 days and 8 months apart')
                            print(error)
                            eval = False
                            with open('gedcom_output.txt', 'a') as f:
                                f.write(error)
                                f.write('\n')
                                f.close()

    return eval

#US16 : Male last names


def us16_male_last_names(Individual, Family):
    error_msg = ''
    ret_val = True
    for fam_detail in Family:
        #print(fam_detail)
        #print('Husband is ',fam_detail[3])

        # get Father's last name to set the base
        for ind_detail in Individual:
            if(fam_detail[3] == ind_detail[0]):
                #print(ind_detail[1].replace('/',''))
                full_name = ind_detail[1].replace('/', '').split(' ')
                #print('full name ', full_name)
                family_last_name = full_name[1]
                #print('family last name ', family_last_name)

        arr_of_children = fam_detail[5].split(' ')
        if(len(arr_of_children) > 0):
            for child in arr_of_children:
                # get children's last name to see if its the same as the father's last name
                for child_detail in Individual:
                    #print(child_detail)
                    if(child == child_detail[0] and child_detail[2] == 'M' and ret_val == True):
                        #print(child_detail[1].replace('/', ''))
                        child_full_name = child_detail[1].replace(
                            '/', '').split(' ')
                        #print('child full name ', child_full_name)
                        child_last_name = child_full_name[1]
                        #print('child last name ', child_last_name)
                        if(child_last_name != family_last_name):
                            error_msg = 'Anomaly US16: All male members of the Family (' + \
                                fam_detail[0] + \
                                ') do not have the same last name'
                            ret_val = False
                            print(error_msg)
                            with open('gedcom_output.txt', 'a') as f:
                                f.write(error_msg)
                                f.write('\n')

    return ret_val

# US21: Correct gender for role


def us21_correct_gender_for_role(Individual, Family):
    error_msg = ''
    ret_val = True
    for fam_detail in Family:
        #print(fam_detail)
        # husband should be in pos 3 and wife should be in pos 4
        # check husband's gender
        for ind_detail in Individual:
            if(fam_detail[3] == ind_detail[0]):
                if(ind_detail[2] != 'M'):
                    error_msg = 'Error US21: Husband (' + ind_detail[0] + \
                        ') in Family (' + \
                        fam_detail[0] + ') has the wrong gender'
                    ret_val = False
                    print(error_msg)
                    with open('gedcom_output.txt', 'a') as f:
                        f.write(error_msg)
                        f.write('\n')

        # check wife's gender
        for ind_detail in Individual:
            if(fam_detail[4] == ind_detail[0]):
                if(ind_detail[2] != 'F'):
                    error_msg = 'Error US21: Wife (' + ind_detail[0] + ') in Family (' + fam_detail[0] + \
                        ') has the wrong gender'
                    ret_val = False
                    print(error_msg)
                    with open('gedcom_output.txt', 'a') as f:
                        f.write(error_msg)
                        f.write('\n')

    return ret_val
