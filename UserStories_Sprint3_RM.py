
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

# Sprint 3

######################################################

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


if __name__ == "__main__":

    # Get the ged file it needs to be in same folder
    #file_path = '/Users/Vicky/Desktop/gedcom_sprint_1.txt'
    #file_path = 'GedcomSp3.ged'
    #file_path = 'gedcom_test1.ged'
    # input parameters
    inputs = len(sys.argv)
    print("Total inputs passed:", inputs)
    file_path = sys.argv[1]
    dataframe = print_indi(file_path)
    dataframe_family = print_fam(file_path, dataframe)
    us10_Marriage_before_14(dataframe, dataframe_family)
    us14_Multiple_Births(dataframe, dataframe_family)
