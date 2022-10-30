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

######################################################

# Sprint 4

######################################################


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


if __name__ == "__main__":

    # Get the ged file it needs to be in same folder
    #file_path = '/Users/Vicky/Desktop/gedcom_sprint_1.txt'
    #file_path = 'GedcomSp3.ged'
    #file_path = 'gedcom_sprint_1.ged'
    # input parameters
    inputs = len(sys.argv)
    print("Total inputs passed:", inputs)
    file_path = sys.argv[1]
    dataframe = print_indi(file_path)
    dataframe_family = print_fam(file_path, dataframe)
    us29_List_Deceased(dataframe, dataframe_family)
    us35_List_Recent_Births(dataframe, dataframe_family)
