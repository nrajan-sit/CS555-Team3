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


if __name__ == "__main__":

    # Get the ged file it needs to be in same folder
    #file_path = '/Users/Vicky/Desktop/gedcom_sprint_1.txt'
    #file_path = 'gedcom_sprint_1.ged'
    #input parameters
    inputs = len(sys.argv)
    print("Total inputs passed:", inputs)

    file_path = sys.argv[1]
    dataframe = print_indi(file_path)
    dataframe_family = print_fam(file_path,dataframe)
    us05_Marriage_before_Death(dataframe, dataframe_family)
    us06_Divorce_before_Death(dataframe, dataframe_family)
