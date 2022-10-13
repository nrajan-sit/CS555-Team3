###############################################################################################

			                            #CS 555 : Team 3


###############################################################################################

# Import collection package
from collections import namedtuple

# Import parameter package
import sys

# Import datetime package
from datetime import datetime
import datetime as dt

import pandas as pd
import numpy as np

from io import StringIO
import prettytable

from UserStories_Sprint1_Team3 import *
from UserStories_Sprint2_Team3 import *



Individual = namedtuple('Individual', 'Individual_ID, Name, Sex, DOB, DOD, FAMC, FAMS')
Family = namedtuple('Family', 'Family_ID, Marriage_Date, Husband_ID, Wife_ID, Child_ID, Divorce_Date, Event_Date')

def gedcom_file_parser_ind(file_name):
    file_contents = open(file_name,'r')
    ind_counter = 0
    ind_id = ''
    ind_name = ''
    ind_sex = ''
    ind_dob = ''
    ind_dod = ''
    ind_famc = ''
    ind_fams = ''
    temp_dob = ''
    Individual_list = []
    previous_tag = ''

    for file_line in file_contents:
        line_details = file_line.split()

        if (len(line_details) > 2):
            #print('---------------------')
            #print('0:', line_details)

            if (line_details[0] == '0' and line_details[2] == 'INDI' ):
                    if ind_counter == 0:
                        ind_id = line_details[1].replace('@',"")
                        ind_counter = 1
                    else:
                        Individual_list.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])
                        ind_id = ''
                        ind_name = ''
                        ind_sex = ''
                        ind_dob = ''
                        ind_dod = ''
                        ind_famc = ''
                        ind_fams = ''
                        ind_id = line_details[1].replace('@',"")

            if (line_details[0] == '1' and line_details[1] == 'NAME'):
                ind_name = line_details[2] + ' ' +line_details[3]

            if (line_details[0] == '1' and line_details[1] == 'SEX'):
                ind_sex = line_details[2]

            if (line_details[0] == '1' and line_details[1] == 'FAMC'):
                ind_famc = "{'" + line_details[2].replace('@',"") + "'}"

            if (line_details[0] == '1' and line_details[1] == 'FAMS'):
                ind_fams += line_details[2].replace('@',"") + ' '

            # Dates are on the next line
            if (line_details[0] == '2' and line_details[1] == 'DATE'):
                if(line_details[3] == 'JAN'):
                    month = '01'
                if(line_details[3] == 'FEB'):
                    month = '02'
                if(line_details[3] == 'MAR'):
                    month = '03'
                if(line_details[3] == 'APR'):
                    month = '04'
                if(line_details[3] == 'MAY'):
                    month = '05'
                if(line_details[3] == 'JUN'):
                    month = '06'
                if(line_details[3] == 'JUL'):
                    month = '07'
                if(line_details[3] == 'AUG'):
                    month = '08'
                if(line_details[3] == 'SEP'):
                    month = '09'
                if(line_details[3] == 'OCT'):
                    month = '10'
                if(line_details[3] == 'NOV'):
                    month = '11'
                if(line_details[3] == 'DEC'):
                    month = '12'
                if previous_tag == 'BIRT':
                    ind_dob = datetime.strptime(line_details[4]+'/'+month+'/'+line_details[2], '%Y/%m/%d').date()
                if previous_tag == 'DEAT':
                    ind_dod = datetime.strptime(line_details[4]+'/'+month+'/'+line_details[2], '%Y/%m/%d').date()

        # store the tag for date calculations
        previous_tag = line_details[1]

    Individual_list.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])
    return Individual_list

def gedcom_file_parser_fam(file_name):
    file_contents = open(file_name,'r')
    fam_counter = 0
    fam_id = ''
    fam_marr = ''
    fam_husb = ''
    fam_wife = ''
    fam_chil = ''
    fam_div = ''
    fam_event = ''
    fam_event_date = ''
    Family_list = []
    previous_tag = ''

    for file_line in file_contents:
        line_details = file_line.split()

        if (len(line_details) > 2):
             #print('---------------------')
             #print('0:', line_details)

            if (line_details[0] == '0' and line_details[2] == 'FAM' ):
                     if fam_counter == 0:
                         fam_id = line_details[1].replace('@',"")
                         fam_counter = 1
                     else:
                         Family_list.append([fam_id, fam_marr, fam_div, fam_husb, fam_wife, fam_chil])
                         fam_id = ''
                         fam_marr = ''
                         fam_husb = ''
                         fam_wife = ''
                         fam_chil = ''
                         fam_div = ''
                         fam_event = ''
                         fam_event_date = ''
                         fam_id = line_details[1].replace('@',"")

            if (line_details[0] == '1' and line_details[1] == 'HUSB'):
                         fam_husb = line_details[2].replace('@',"")
            if (line_details[0] == '1' and line_details[1] == 'WIFE'):
                         fam_wife = line_details[2].replace('@',"")

            if (line_details[0] == '1' and line_details[1] == 'CHIL'):
                         fam_chil += line_details[2].replace('@',"")+' '

            if (line_details[0] == '2' and line_details[1] == 'DATE'):
                        if(line_details[3] == 'JAN'):
                            month = '01'
                        if(line_details[3] == 'FEB'):
                            month = '02'
                        if(line_details[3] == 'MAR'):
                            month = '03'
                        if(line_details[3] == 'APR'):
                            month = '04'
                        if(line_details[3] == 'MAY'):
                            month = '05'
                        if(line_details[3] == 'JUN'):
                            month = '06'
                        if(line_details[3] == 'JUL'):
                            month = '07'
                        if(line_details[3] == 'AUG'):
                            month = '08'
                        if(line_details[3] == 'SEP'):
                            month = '09'
                        if(line_details[3] == 'OCT'):
                            month = '10'
                        if(line_details[3] == 'NOV'):
                            month = '11'
                        if(line_details[3] == 'DEC'):
                            month = '12'
                        if previous_tag == 'MARR':
                            fam_marr = datetime.strptime(line_details[4]+'/'+month+'/'+line_details[2], '%Y/%m/%d').date()
                        if previous_tag == 'DIV':
                            fam_div = datetime.strptime(line_details[4]+'/'+month+'/'+line_details[2], '%Y/%m/%d').date()

         # store the tag for date calculations
        previous_tag = line_details[1]

    Family_list.append([fam_id, fam_marr, fam_div, fam_husb, fam_wife, fam_chil])
    return Family_list

def list_to_str(ls):
    ls = ls.split(' ')[:-1]
    flag = 0
    op = "{"
    for i in ls:
        if flag == 0:
            op += "'"+str(i)+"'"
            flag = 1
        else:
            op += ','+"'"+str(i)+"'"


    op += "}"

    if op == '{}':
        op = 'NA'

    return op


def print_indi(file_path):
    #fam = gedcom_file_parser_fam(file_path)
    inds = gedcom_file_parser_ind(file_path)

    dataframe = pd.DataFrame(inds)

    dataframe.columns = ['ID','Name','Gender','Birthday','Death','Child','Spouse']
    dataframe.sort_values(by=['ID'])

    age = datetime.today().date() - dataframe['Birthday']
    age = age.apply(lambda x: int(x.days/365))
    dataframe.insert(4, "Age",age , True)
    dataframe = dataframe.replace('','NA')
    dataframe.insert(5, "Alive",dataframe['Death']=='NA' , True)

    spouses = dataframe['Spouse'].apply(list_to_str)
    dataframe = dataframe.drop('Spouse',axis=1)

    if __name__ == "__main__":
        output = StringIO()
        dataframe.set_index('ID').to_csv(output)
        output.seek(0)
        pt = prettytable.from_csv(output)
        pt.add_column("Spouse",spouses)
        print('Individuals')
        print (pt)
        with open('gedcom_output.txt', 'a') as f:
            f.write(str(pt))
            f.write('\n')
    return(dataframe)

def print_fam(file_path,dataframe):
    fam = gedcom_file_parser_fam(file_path)
    dataframe_family = pd.DataFrame(fam)
    dataframe_family.columns = ['ID','Married','Divorced','Husband ID','Wife ID','Children']
    #dataframe_family.sort_values(by='ID')

    #dataframe_family['new'] = dataframe_family['ID'].str.extract('(\d+)').astype(int)
    #dataframe_family = dataframe_family.sort_values(by=['new'], ascending=True).drop('new', axis=1)

    dataframe_family = dataframe_family.replace('','NA')

    husband_id = np.array(dataframe_family['Husband ID'])
    husband_array = []
    for h in husband_id:
        husband_array.append(dataframe.loc[dataframe['ID'] == h]['Name'].values[0])

    dataframe_family.insert(4, "Husband Name",husband_array , True)

    wife_id = np.array(dataframe_family['Wife ID'])
    wife_array = []
    for w in wife_id:
        wife_array.append(dataframe.loc[dataframe['ID'] == w]['Name'].values[0])

    dataframe_family.insert(6, "Wife Name",wife_array , True)
    cldn = dataframe_family['Children'].apply(list_to_str)
    dataframe_family = dataframe_family.drop('Children',axis=1)

    if __name__ == "__main__":
        output = StringIO()
        dataframe_family.set_index('ID').to_csv(output)
        output.seek(0)
        ptf = prettytable.from_csv(output)
        ptf.add_column("Children",cldn)
        print('Families')
        ptf.sortby = "ID"
        print (ptf)
        with open('gedcom_output.txt', 'a') as f:
            f.write(str(ptf))
            f.write('\n')
    return (dataframe_family)



#####################################
# Main
#####################################

if __name__ == "__main__":

    # Get the ged file it needs to be in same folder
    file_path = 'gedcom_sprint_2.ged'

    # input parameters
    #inputs = len(sys.argv)
    #print("Total inputs passed:", inputs)

    #file_path = sys.argv[1]

    # Get all the individual's details
    inds = gedcom_file_parser_ind(file_path)

    # Get all the family details
    fam = gedcom_file_parser_fam(file_path)

    f = open('gedcom_output.txt', 'w')

    dataframe = print_indi(file_path)
    dataframe_family = print_fam(file_path,dataframe)

    #########Sprint1########
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

    ########Sprint2########
    #US05
    us05_Marriage_before_Death(dataframe, dataframe_family)

    #US06
    us06_Divorce_before_Death(dataframe, dataframe_family)

    #US07
    us07_less_than_150yrs(inds)

    #US08
    us08_birth_before_marriage_of_parents(inds,fam)

    #US17
    us17_no_marriage_to_descendants(fam)

    #US18
    us18_no_marriage_between_siblings(fam)

    f.close()
