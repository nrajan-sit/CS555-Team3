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


#US07 : Less then 150 years old
def us07_less_than_150yrs(Individual):
    error_msg = ''
    ret_val = False
    for i in Individual:

        current_age = 0
        #print(i[3])
        if (i[3] != '' and i[4] == ''):
            today = date.today()
            current_age = today.year - \
                i[3].year - ((today.month, today.day) < (i[3].month, i[3].day))
            #print('Person still alive')
            #print('current age is ' , current_age)
            if (current_age >= 150):
                ret_val = True
                error_msg = 'Anomaly US07: ' + i[1] + ' is over 150 yrs old'
                print(error_msg)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error_msg)
                    f.write('\n')

        elif (i[3] != '' and i[4] != ''):
            current_age = i[4].year - i[3].year - \
                ((i[4].month, i[4].day) < (i[3].month, i[3].day))
            #print('Person is dead')
            #print('current age is ' , current_age)
            if (current_age >= 150):
                ret_val = True
                error_msg = 'Anomaly US07: ' + \
                    i[1].replace('/', '') + ' is over 150 yrs old'
                print(error_msg)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error_msg)
                    f.write('\n')

        else:
            ret_val = False

    return ret_val

# US08	Birth before marriage of parents
def us08_birth_before_marriage_of_parents(Individual, Family):
    error_msg = ''
    ret_val = False
    for i in Family:
        #print(i)
        if (i[1] != '' and i[2] == ''):
            #print(i[5])
            arr_of_children = i[5].split(' ')
            #print(arr_of_children)
            if(len(arr_of_children) > 0):
                #print(arr_of_children)
                for child in arr_of_children:
                    for inds in Individual:
                        if(inds[0] == child):
                            _gender = ''
                            #print('same person', inds[0], child, inds)
                            if(i[1] > inds[3]):
                                if(inds[2] == 'M'):
                                    _gender = 'his'
                                if(inds[2] == 'F'):
                                    _gender = 'her'

                                error_msg = 'Anomaly US08: Birth date of ' + \
                                    inds[1].replace(
                                        '/', '') + ' (' + inds[0] + ') occurs after the marriage date of ' + _gender + ' parents in Family (' + i[0] + ')'
                                ret_val = True
                                print(error_msg)
                                with open('gedcom_output.txt', 'a') as f:
                                    f.write(error_msg)
                                    f.write('\n')

        elif (i[1] != '' and i[2] != ''):  # and i[2] > i[1]):
            #print(i)
            arr_of_children = i[5].split(' ')
            #print(arr_of_children)
            if(len(arr_of_children) > 0):
                for child in arr_of_children:
                    for inds in Individual:
                        if(inds[0] == child):
                            _gender = ''
                            #print('same person', inds[0], child, inds)
                            num_months = (inds[3].year - i[2].year) * \
                                12 + (inds[3].month - i[2].month)
                            #print(i[2], inds[3], num_months)
                            if(i[2] < inds[3] and num_months < 9):
                                if(inds[2] == 'M'):
                                    _gender = 'his'
                                if(inds[2] == 'F'):
                                    _gender = 'her'

                                error_msg = 'Anomaly US08: Birth date of ' + \
                                    inds[1].replace(
                                        '/', '') + ' (' + inds[0] + ') occurs after the divorce date of ' + _gender + ' parents in Family (' + i[0] + ')'
                                ret_val = True
                                print(error_msg)
                                with open('gedcom_output.txt', 'a') as f:
                                    f.write(error_msg)
                                    f.write('\n')

        else:
            ret_val = False

    return ret_val

def us05_Marriage_before_Death(individuals, families):

    return_flag = True
    error_type = "US05"

    for i in range(len(families)):
        married_date = families.iloc[[i]]['Married'].values[0]
        h_id = families.iloc[[i]]['Husband ID'].values[0]
        w_id = families.iloc[[i]]['Wife ID'].values[0]


        if (individuals.loc[individuals['ID'] == h_id]['Alive'].values == False)[0]:
            if (individuals.loc[individuals['ID'] == h_id]['Death'].values[0]) < married_date:
                name = individuals.loc[individuals['ID'] == h_id]['Name'].values[0].replace('/','')
                er_message = 'Error {}: Death date of {} ({}) occurs before Marriage date'.format(error_type,name,h_id)
                print(er_message)
                with open('gedcom_output.txt', 'a') as f:
                        f.write(er_message)
                        f.write('\n')
                        f.close()

                return_flag = False
        if (individuals.loc[individuals['ID'] == w_id]['Alive'].values == False)[0]:
            if (individuals.loc[individuals['ID'] == w_id]['Death'].values[0]) < married_date:
                name = individuals.loc[individuals['ID'] == w_id]['Name'].values[0].replace('/','')
                er_message = 'Error {}: Death date of {} ({}) occurs before Marriage date'.format(error_type,name,w_id)
                print(er_message)
                with open('gedcom_output.txt', 'a') as f:
                        f.write(er_message)
                        f.write('\n')
                        f.close()
                return_flag = False

    return return_flag

def us06_Divorce_before_Death(individuals, families):
    # For each individual check if divorce occurs before death
    return_flag = True
    error_type = "US06"

    dff = families
    divor = list(dff['Divorced'].replace('NA',pd.NA).dropna().index)

    for i in divor:


        divorced_date = families.iloc[[i]]['Divorced'].values[0]
        h_id = families.iloc[[i]]['Husband ID'].values[0]
        w_id = families.iloc[[i]]['Wife ID'].values[0]


        if (individuals.loc[individuals['ID'] == h_id]['Alive'].values == False)[0]:
            if (individuals.loc[individuals['ID'] == h_id]['Death'].values[0]) < divorced_date:
                name = individuals.loc[individuals['ID'] == h_id]['Name'].values[0].replace('/','')
                er_message = 'Error {}: Death date of {} ({}) occurs after Divorce date'.format(error_type,name,h_id)
                print(er_message)
                with open('gedcom_output.txt', 'a') as f:
                        f.write(er_message)
                        f.write('\n')
                        f.close()

                return_flag = False


        if (individuals.loc[individuals['ID'] == w_id]['Alive'].values == False)[0]:
            if (individuals.loc[individuals['ID'] == w_id]['Death'].values[0]) < divorced_date:
                name = individuals.loc[individuals['ID'] == w_id]['Name'].values[0].replace('/','')
                er_message = 'Error {}: Death date of {} ({}) occurs after Divorce date'.format(error_type,name,w_id)
                print(er_message)
                with open('gedcom_output.txt', 'a') as f:
                        f.write(er_message)
                        f.write('\n')
                        f.close()
                return_flag = False

    return return_flag


#US17 No marriage to descendants
def us17_no_marriage_to_descendants(Family):

    child_id = ''
    husband_id = ''
    wife_id =''
    family_id = ''
    eval = True

    for i in Family:
        children_id = i[5].split()
        family_id = i[0]
        husband_id = i[3]
        wife_id = i[4]

        for c in children_id:
            if (c == husband_id):
                error = 'Error US17: Wife (' + wife_id + ') of family ('+family_id +') is married to her child ('+c+').'
                print(error)
                eval = False
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error)
                    f.write('\n')
                    f.close()

            if (c == wife_id):
                error = 'Error US17: Husband (' + husband_id + ') of family ('+family_id +') is married to his child ('+c+').'
                print(error)
                eval = False
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error)
                    f.write('\n')
                    f.close()

    return eval


#US18 siblings should not marry
def us18_no_marriage_between_siblings(Family):

    eval = True
    husband_id = ''
    wife_id = ''
    husband_birth_family = '#'
    wife_birth_family = ''
    marriage_family = ''

    for i in Family:
        husband_id = i[3]
        wife_id = i[4]
        marriage_family = i[0]

        for j in Family:

            children_id = j[5].split()

            for c in children_id:
                if (husband_id == c):
                    husband_birth_family = j[0]

                if(wife_id == c):
                    wife_birth_family = j[0]


        if (husband_birth_family == wife_birth_family):
           anomaly = 'Anomaly US18: Siblings from family (' + wife_birth_family +') are married to each other in family ('+ marriage_family+').'
           eval = False
           print(anomaly)
           with open('gedcom_output.txt', 'a') as f:
               f.write(anomaly)
               f.write('\n')
               f.close()

    return eval
