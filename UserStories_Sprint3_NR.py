from gedcom import *
from datetime import date

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
                        child_full_name = child_detail[1].replace('/', '').split(' ')
                        #print('child full name ', child_full_name)
                        child_last_name = child_full_name[1]
                        #print('child last name ', child_last_name)
                        if(child_last_name != family_last_name):
                            error_msg = 'Anomaly US16: All male members of the Family (' + fam_detail[0]  + ') do not have the same last name'
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
                        ') in Family (' + fam_detail [0] + ') has the wrong gender'
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
