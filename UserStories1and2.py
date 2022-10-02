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



def dates_before_current(individuals, families):
    return_flag = True
    error_type = "US01"

    if any(individuals['Birthday']> datetime.today().date()):
        wrong_entries = individuals[list((individuals['Birthday'] > datetime.today().date())==True)]
        wr = list(wrong_entries[['ID','Name']].values)
        for w in wr:
            print('Error {}: Birth date of {} ({}) occurs after current date'.format(error_type,w[1].replace('/',''),w[0]))

        return_flag = False

    df = individuals
    dead = df['Death'].replace('NA',pd.NA).dropna()
    
    if any(dead > datetime.today().date()):
    
        wrong_entries = df['Death'].replace('NA',pd.NA).dropna().index
        
        for w in wrong_entries:
            wr_name = df.iloc[[w]]['Name'].values[0]
            wr_id = df.iloc[[w]]['ID'].values[0]
            
            print('Error {}: Death date of {} ({}) occurs after current date'.format(error_type,wr_name.replace('/',''),wr_id))

        return_flag = False
    
    if any(families['Married']> datetime.today().date()):
        wrong_entries = families[list((families['Married'] > datetime.today().date())==True)]
        wr = list(wrong_entries[['ID','Husband Name','Wife Name']].values)
        for w in wr:
            print('Error {}: Marriage date of {} and {} ({}) occurs after current date'.format(error_type,w[1].replace('/',''),w[2].replace('/',''),w[0]))

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
            
            print('Error {}: Divorce date of {} and {} ({}) occurs after current date'.format(error_type,wr_name_h.replace('/',''),wr_name_w.replace('/',''),wr_id))

        return_flag = False
    
    return return_flag

def birth_before_marriage(individuals, families):
    return_flag = True
    error_type = "US02"

    for i in range(len(families)):
        married_date = families.iloc[[i]]['Married'].values[0]
        h_id = families.iloc[[i]]['Husband ID'].values[0]
        w_id = families.iloc[[i]]['Wife ID'].values[0]

        
        if (individuals.loc[individuals['ID'] == h_id]['Birthday'].values[0]) > married_date:
            name = individuals.loc[individuals['ID'] == h_id]['Name'].values[0].replace('/','')
            print('Error {}: Birth date of {} ({}) occurs after Marriage date'.format(error_type,name,h_id))
            return_flag = False

        if (individuals.loc[individuals['ID'] == w_id]['Birthday'].values[0]) > married_date:
            name = individuals.loc[individuals['ID'] == w_id]['Name'].values[0].replace('/','')
            print('Error {}: Birth date of {} ({}) occurs after Marriage date'.format(error_type,name,w_id))
            return_flag = False

    return return_flag

if __name__ == "__main__":  
    
    # Get the ged file it needs to be in same folder
    #file_path = 'ged_input_file_test.ged'
    
    #input parameters
    inputs = len(sys.argv)
    print("Total inputs passed:", inputs)
    
    file_path = sys.argv[1]
    dataframe = print_indi(file_path)
    dataframe_family = print_fam(file_path,dataframe)
    dates_before_current(dataframe,dataframe_family)
    birth_before_marriage(dataframe, dataframe_family)