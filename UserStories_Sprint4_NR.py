from datetime import date, timedelta
from gedcom import *


#US36 : List recent deaths
def us36_list_recent_deaths(Individual):
    listToStr = ''
    ret_ind = []
    ret_val = False
    for ind_detail in Individual:
        #print(ind_detail)
        #print('Death ', ind_detail[4])
        ret_val = False
        
        if(ind_detail[4] != ''):
            current_date = date.today()
            
            if current_date - timedelta(days=30) <= ind_detail[4] <= current_date :
                ret_ind.append(ind_detail[1].replace( '/', '') + ' (' + ind_detail[0] + ') has passed away recently')
                #print("in between")
                listToStr = '\n'.join([str(elem) for elem in ret_ind])
                ret_val = True

    #print(listToStr)
    with open('gedcom_output.txt', 'a') as f:
        f.write(listToStr)
        f.write('\n')
        
    return ret_ind

# US38 : List upcoming birthdays
def us38_list_upcoming_birthdays(Individual):
    listToStr = ''
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
            ret_ind.append(ind_detail[1].replace('/','') + ' (' + ind_detail[0] + ') has an upcoming birthday')
            #print("in between")
            listToStr = '\n'.join([str(elem) for elem in ret_ind])
            ret_val = True

    #print(listToStr)
    with open('gedcom_output.txt', 'a') as f:
        f.write(listToStr)
        f.write('\n')
            
    return listToStr
