# Import collection package
from collections import namedtuple

# Import parameter package
import sys

# Import datetime package
from datetime import datetime
import datetime as dt
from datetime import date, timedelta

import pandas as pd
import numpy as np

from gedcom import *


def us29_List_Deceased(individuals, families):

    return_flag = False
    user_story = "US29"

    df = individuals
    dead = list(df['Death'].replace('NA', pd.NA).dropna().index)

    for i in dead:
        ind_id = individuals.iloc[[i]]['ID'].values[0]
        ind_name = individuals.iloc[[i]]['Name'].values[0].replace('/', '')
        message = '{}: {} ({}) is dead.'.format(user_story, ind_name, ind_id)
        print(message)
        with open('gedcom_output.txt', 'a') as f:
            f.write(message)
            f.write('\n')
            f.close()
        return_flag = True

    return return_flag


def us35_List_Recent_Births(individuals, families):

    return_flag = False
    user_story = "US35"

    recent_births = individuals[datetime.date(
        datetime.today()) - individuals['Birthday'] <= dt.timedelta(30)]

    for i in list(recent_births.index):
        ind_id = individuals.iloc[[i]]['ID'].values[0]
        ind_name = individuals.iloc[[i]]['Name'].values[0].replace('/', '')
        message = '{}: {} ({}) was born in last 30 days.'.format(
            user_story, ind_name, ind_id)
        print(message)
        with open('gedcom_output.txt', 'a') as f:
            f.write(message)
            f.write('\n')
            f.close()
        return_flag = True

    return return_flag


#US36 : List recent deaths
def us36_list_recent_deaths(Individual):
    output = ''
    ret_ind = []
    ret_val = False
    for ind_detail in Individual:
        #print(ind_detail)
        #print('Death ', ind_detail[4])
        ret_val = False

        if(ind_detail[4] != ''):
            current_date = date.today()

            if current_date - timedelta(days=30) <= ind_detail[4] <= current_date:
                ret_ind.append(ind_detail[1].replace(
                    '/', '') + ' (' + ind_detail[0] + ') has passed away recently')
                #print("in between")
                #listToStr = '\n'.join([str(elem) for elem in ret_ind])
                output = 'US36: ' + ind_detail[1].replace('/', '') + ' (' + ind_detail[0] + ') has passed away recently'
                print(output)
                ret_val = True

    #print(listToStr)
    with open('gedcom_output.txt', 'a') as f:
        f.write(output)
        f.write('\n')

    return ret_ind


# US38 : List upcoming birthdays
def us38_list_upcoming_birthdays(Individual):
    output = ''
    ret_ind = []
    ret_val = False
    for ind_detail in Individual:
        #print(ind_detail)
        #print('Birthday ', ind_detail[3])
        ret_val = False
        current_date = date.today()
        modified_bday = ind_detail[3].replace(year=current_date.year)

        #print('modified_bday ', modified_bday)

        if current_date <= modified_bday <= current_date + timedelta(days=30):
            ret_ind.append(ind_detail[1].replace(
                '/', '') + ' (' + ind_detail[0] + ') has an upcoming birthday')
            #print("in between")
            output = 'US38: ' + ind_detail[1].replace('/', '') + ' (' + ind_detail[0] + ') has an upcoming birthday'
            print(output)
            #listToStr = '\n'.join([str(elem) for elem in ret_ind])
            #print(listToStr)
            ret_val = True

    #print(listToStr)
    with open('gedcom_output.txt', 'a') as f:
        f.write(output)
        f.write('\n')

    return output


#US31 List Living Single: List all living people over 30 who have never been
#married in a GEDCOM file
def us31_list_living_single(Individual):
    living_single_name = []
    living_single_id = []
    eval = False

    for i in Individual:
        if (i[4] == ''):
            person_id = i[0]
            person_name = i[1].replace('/', "")
            person_birthday = i[3]

            today = date.today()
            person_age = today.year - person_birthday.year - \
                ((today.month, today.day) <
                 (person_birthday.month, person_birthday.day))

            if(person_age > 30):
                if (i[6] == ''):
                    living_single_name.append(person_name)
                    living_single_id.append(person_id)
                    eval = True

    opening_sentence = (
        'US31: These individuals are alive, over 30 and never been married: ')
    print(opening_sentence, end="")
    with open('gedcom_output.txt', 'a') as f:
        f.write(opening_sentence)

    for j, k in zip(living_single_name, living_single_id):
        print(j+'('+k+') ', end="")
        with open('gedcom_output.txt', 'a') as f:
            f.write(j+' ('+k+') ')

    print('.')
    with open('gedcom_output.txt', 'a') as f:
        f.write('.\n')

    return eval


#US30 List Living Married: List all living married people in a GEDCOM file
def us30_list_living_married(Individual, Family):
    living_married_name = []
    living_married_id = []
    eval = False

    for i in Individual:
        if (i[4] == ''):
            person_id = i[0]
            person_name = i[1].replace('/', "")

            if (i[6] != ''):
                spouses = i[6].split()

                for s in spouses:
                    for f in Family:
                        if ((s == f[0]) and (f[2] == '')):

                            if(person_id == f[3]):
                                for m in Individual:
                                    if((f[4] == m[0]) and (m[4] == '')):
                                        eval = True
                                        living_married_name.append(person_name)
                                        living_married_id.append(person_id)

                            if(person_id == f[4]):
                                for n in Individual:
                                    if((f[3] == n[0]) and (n[4] == '')):
                                        eval = True
                                        living_married_name.append(person_name)
                                        living_married_id.append(person_id)

    opening_sentence = ('US30: These individuals are alive and married: ')
    print(opening_sentence, end="")
    with open('gedcom_output.txt', 'a') as f:
        f.write(opening_sentence)

    for j, k in zip(living_married_name, living_married_id):
        print(j+'('+k+') ', end="")
        with open('gedcom_output.txt', 'a') as f:
            f.write(j+' ('+k+') ')

    print('.')
    with open('gedcom_output.txt', 'a') as f:
        f.write('.\n')

    return eval
