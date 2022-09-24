###############################################################################################

			                            #CS 555 : Team 3


###############################################################################################

# Import collection package
from collections import namedtuple

# Import parameter package
import sys

# Import datetime package
from datetime import datetime

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
                        ind_id = line_details[1]
                        ind_counter = 1
                    else:
                        Individual_list.append(Individual(ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams))
                        ind_id = ''
                        ind_name = ''
                        ind_sex = '' 
                        ind_dob = ''
                        ind_dod = ''
                        ind_famc = ''
                        ind_fams = ''
                        ind_id = line_details[1]
    
            if (line_details[0] == '1' and line_details[1] == 'NAME'):
                ind_name = line_details[2] + ' ' +line_details[3].replace("/", "")
                    
            if (line_details[0] == '1' and line_details[1] == 'SEX'):
                ind_sex = line_details[2]
                
            if (line_details[0] == '1' and line_details[1] == 'FAMC'):
                ind_famc = line_details[2]
                
            if (line_details[0] == '1' and line_details[1] == 'FAMS'):
                ind_fams = line_details[2]
                
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
            
    Individual_list.append(Individual(ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams))
    return Individual_list
    
# TODO    
# def gedcom_file_parser_fam(file_name):
#     file_contents = open(file_name,'r')
#     fam_counter = 0
#     fam_id = ''
#     fam_marr = ''
#     fam_husb = ''
#     fam_wife = ''
#     fam_chil = ''
#     fam_div = ''
#     fam_event = ''
#     fam_event_date = ''
#     Family_list = []
#     previous_tag = ''
    
#     for file_line in file_contents:
#         line_details = file_line.split()
        
#         if (len(line_details) > 2):
#             #print('---------------------')
#             #print('0:', line_details)
            
#             if (line_details[0] == '0' and line_details[2] == 'FAM' ):
#                     if fam_counter == 0:
#                         fam_id = line_details[1]
#                         fam_counter = 1
#                     else:
#                         Family_list.append(Family(fam_id, fam_marr, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams))
#                         fam_id = ''
#                         fam_marr = ''
#                         fam_husb = ''
#                         fam_wife = ''
#                         fam_chil = ''
#                         fam_div = ''
#                         fam_event = ''
#                         fam_event_date = ''
#                         fam_id = line_details[1]
    
            
#         # store the tag for date calculations
#         previous_tag = line_details[1]
            
#     Family_list.append(Family(fam_id, fam_marr, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams))
#     return Family_list    
#####################################
# Main
#####################################

if __name__ == "__main__":  
    
    # Get the ged file
    #file_path = 'Test_3.ged'
    
    # input parameters
    inputs = len(sys.argv)
    print("Total inputs passed:", inputs)
    
    file_path = sys.argv[1]
    
    # Get all the individual's details
    inds = gedcom_file_parser_ind(file_path)
    
    # Get all the family details
    #fam = gedcom_file_parser_fam(file_path)
    
    for i in inds:
        print(i)