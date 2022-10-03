# Import collection package
from collections import namedtuple

# Import parameter package
import sys

# Import datetime package
from datetime import datetime
import datetime as dt

import pandas as pd
import numpy as np

from gedcom import *


######## US01 ########
def dates_before_current(individuals, families):
    return_flag = True
    error_type = "US01"

    if any(individuals['Birthday']> datetime.today().date()):
        wrong_entries = individuals[list((individuals['Birthday'] > datetime.today().date())==True)]
        wr = list(wrong_entries[['ID','Name']].values)
        for w in wr:
            er_message = 'Error {}: Birth date of {} ({}) occurs after current date'.format(error_type,w[1].replace('/',''),w[0])
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                    f.write(er_message)
                    f.write('\n')
                    f.close()
        return_flag = False

    df = individuals
    dead = df['Death'].replace('NA',pd.NA).dropna()

    if any(dead > datetime.today().date()):

        wrong_entries = df['Death'].replace('NA',pd.NA).dropna().index

        for w in wrong_entries:
            wr_name = df.iloc[[w]]['Name'].values[0]
            wr_id = df.iloc[[w]]['ID'].values[0]

            er_message = 'Error {}: Death date of {} ({}) occurs after current date'.format(error_type,wr_name.replace('/',''),wr_id)
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                    f.write(er_message)
                    f.write('\n')
                    f.close()

        return_flag = False

    if any(families['Married']> datetime.today().date()):
        wrong_entries = families[list((families['Married'] > datetime.today().date())==True)]
        wr = list(wrong_entries[['ID','Husband Name','Wife Name']].values)
        for w in wr:
            er_message = 'Error {}: Marriage date of {} and {} ({}) occurs after current date'.format(error_type,w[1].replace('/',''),w[2].replace('/',''),w[0])
            print()
            with open('gedcom_output.txt', 'a') as f:
                    f.write(er_message)
                    f.write('\n')
                    f.close()

        return_flag = False

    df = families
    divor = df['Divorced'].replace('NA',pd.NA).dropna()

    if any(divor > datetime.today().date()):
        wrong_entries = df['Divorced'].replace('NA',pd.NA).dropna().index


        for w in wrong_entries:
            #wr = list(wrong_entries[['ID','Husband Name','Wife Name']].values)
            wr_name_h = df.iloc[[w]]['Husband Name'].values[0]
            wr_name_w = df.iloc[[w]]['Wife Name'].values[0]
            wr_id = df.iloc[[w]]['ID'].values[0]

            er_message = 'Error {}: Divorce date of {} and {} ({}) occurs after current date'.format(error_type,wr_name_h.replace('/',''),wr_name_w.replace('/',''),wr_id)
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                    f.write(er_message)
                    f.write('\n')
                    f.close()

        return_flag = False

    return return_flag


######## US02 ########
def birth_before_marriage(individuals, families):
    return_flag = True
    error_type = "US02"

    for i in range(len(families)):
        married_date = families.iloc[[i]]['Married'].values[0]
        h_id = families.iloc[[i]]['Husband ID'].values[0]
        w_id = families.iloc[[i]]['Wife ID'].values[0]


        if (individuals.loc[individuals['ID'] == h_id]['Birthday'].values[0]) > married_date:
            name = individuals.loc[individuals['ID'] == h_id]['Name'].values[0].replace('/','')
            er_message = 'Error {}: Birth date of {} ({}) occurs after Marriage date'.format(error_type,name,h_id)
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                    f.write(er_message)
                    f.write('\n')
                    f.close()

            return_flag = False

        if (individuals.loc[individuals['ID'] == w_id]['Birthday'].values[0]) > married_date:
            name = individuals.loc[individuals['ID'] == w_id]['Name'].values[0].replace('/','')
            er_message = 'Error {}: Birth date of {} ({}) occurs after Marriage date'.format(error_type,name,w_id)
            print(er_message)
            with open('gedcom_output.txt', 'a') as f:
                    f.write(er_message)
                    f.write('\n')
                    f.close()
            return_flag = False

    return return_flag


######## US09 ########
def birth_before_parents_death(Individual, Family):

    parent1_death = ''
    parent2_death = ''
    child_birth = ''
    child_name = ''
    eval = True

    for i in Family:
        for j in Individual:
            if (i[3] == j[0]):
                parent1_death = j[4]


            if (i[4] == j[0]):
                parent2_death = j[4]


        children_id = i[5].split()

        if(parent1_death != ''):
            for c in children_id:
                for d in Individual:
                    if (c == d[0]):
                        child_birth = d[3]
                        child_id = d[0]
                        child_name = d[1].replace('/',"")
                        child_gender = ''
                        if (d[2] == 'M'):
                            child_gender = 'his'
                        if (d[2] == 'F'):
                            child_gender = 'her'


                        if (parent1_death <= child_birth):
                            error=("Error US09: Birthday of " + child_name + " ("+ child_id + ") occurs after " + child_gender + " father's death")
                            print(error)
                            eval = False
                            with open('gedcom_output.txt', 'a') as f:
                                f.write(error)
                                f.write('\n')
                                f.close()


        if(parent2_death != ''):
            for c in children_id:
                for d in Individual:
                    if (c == d[0]):
                        child_birth = d[3]
                        child_id = d[0]
                        child_name = d[1].replace('/',"")
                        child_gender = ''
                        if (d[2] == 'M'):
                            child_gender = 'his'
                        if (d[2] == 'F'):
                            child_gender = 'her'

                        if (parent2_death <= child_birth):
                            error = ("Error US09: Birthday of " + child_name + " ("+ child_id + ") occurs after " + child_gender + " mother's death")
                            print(error)
                            eval = False
                            with open('gedcom_output.txt', 'a') as f:
                                f.write(error)
                                f.write('\n')
                                f.close()


    return eval

######## US12 ########
def parents_too_old(Individual, Family):

    husband_birth = ''
    wife_birth = ''
    child_birth = ''
    child_name = ''
    eval = True


    for i in Family:
        for j in Individual:
            if (i[3] == j[0]):
                husband_birth = j[3]
                husband_birth_int = husband_birth.year + husband_birth.month+husband_birth.day


            if (i[4] == j[0]):
                wife_birth = j[3]
                wife_birth_int = wife_birth.year + wife_birth.month +wife_birth.day
                #print(wife_birth_int)


        children_id = i[5].split()

        for c in children_id:
            for d in Individual:
                if (c == d[0]):
                    child_birth = d[3]
                    child_id = d[0]
                    child_birth_int = child_birth.year + child_birth.month+ child_birth.day
                    #print(child_birth_int)
                    child_name = d[1].replace('/',"")
                    difference = child_birth_int - husband_birth_int

                    if (difference >= 80):
                        anomaly = ("Anomaly US12: Father of " + child_name +" (" +child_id+ ") is 80 years older than " + child_name)
                        print(anomaly)
                        eval = False
                        with open('gedcom_output.txt', 'a') as f:
                            f.write(anomaly)
                            f.write('\n')
                            f.close()


        for c in children_id:
            for d in Individual:
                if (c == d[0]):
                    child_birth = d[3]
                    child_id = d[0]
                    child_birth_int = child_birth.year + child_birth.month+ child_birth.day
                    child_name = d[1].replace('/',"")
                    difference = child_birth_int - wife_birth_int

                    if (difference >= 60):
                        anomaly = ("Anomaly US12: Mother of " + child_name + " (" + child_id + ") is 60 years older than " + child_name)
                        print(anomaly)
                        eval = False
                        with open('gedcom_output.txt', 'a') as f:
                            f.write(anomaly)
                            f.write('\n')
                            f.close()

    return eval


######## US03 ########
def us03_birth_before_death(Individual):
    error_msg = ''
    ret_val = True
    for i in Individual:
        _gender = ''
        #print('Birth date of ', i[1].replace('/', ''), ' is ', i[3])
        if (i[4] != ''):
            if(i[3] > i[4]):
                if(i[2] == 'M'):
                    _gender = 'his'
                if(i[2] == 'F'):
                    _gender = 'her'
                error_msg = 'Error US03: Birth date of ' + \
                    i[1].replace('/', '') + ' (' + i[0] + ') ' + \
                    'occurs after ' + _gender + ' death date'
                ret_val = False
                print(error_msg)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error_msg)
                    f.write('\n')
                    f.close()
    return ret_val

######## US04 ########
def us04_marriage_before_divorce(Family):
    error_msg = ''
    ret_val = True
    for i in Family:
        #print(i)
        if (i[2] != ''):
            if(i[1] > i[2]):
                error_msg = 'Error US04: Marriage of Family ' + \
                    i[0] + ' occurs after their divorce date'
                ret_val = False
                print(error_msg)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error_msg)
                    f.write('\n')
                    f.close()
    return ret_val


################### Main ######################################################
if __name__ == "__main__":

    # Get the ged file it needs to be in same folder
    #file_path = '/Users/Vicky/Desktop/gedcom_sprint_1.txt'

    #input parameters
    inputs = len(sys.argv)
    print("Total inputs passed:", inputs)

    file_path = sys.argv[1]

    # Get all the individual's details
    inds = gedcom_file_parser_ind(file_path)

    # Get all the family details
    fam = gedcom_file_parser_fam(file_path)

    dataframe = print_indi(file_path)
    dataframe_family = print_fam(file_path,dataframe)

    f = open('gedcom_output.txt', 'w')

    #US01
    dates_before_current(dataframe,dataframe_family)

    #US02
    birth_before_marriage(dataframe, dataframe_family)

    #US03
    us03_birth_before_death(inds)

    #US04
    us04_marriage_before_divorce(fam)

    #US09
    birth_before_parents_death(inds, fam)

    #US12
    parents_too_old(inds,fam)
