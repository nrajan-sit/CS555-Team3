from gedcom import *
from datetime import date

#US07 : Less then 150 years old
def us07_less_than_150yrs(Individual):
    error_msg = ''
    ret_val = False
    for i in Individual:
        
        current_age = 0
        #print(i[3])
        if (i[3] != '' and i[4] == ''):
            today = date.today()
            current_age = today.year - i[3].year - ((today.month, today.day) < (i[3].month, i[3].day))
            #print('Person still alive')
            #print('current age is ' , current_age)
            if (current_age >= 150):
                ret_val = True
                error_msg = 'Anomaly US07: ' + i[1] + ' is over 150 yrs old'
                print(error_msg)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error_msg)
                    f.write('\n')
        
        elif (i[3] != '' and i[4] != ''):
            current_age = i[4].year - i[3].year - ((i[4].month, i[4].day) < (i[3].month, i[3].day))
            #print('Person is dead')
            #print('current age is ' , current_age)
            if (current_age >= 150):
                ret_val = True
                error_msg = 'Anomaly US07: ' + \
                    i[1].replace('/', '') + ' is over 150 yrs old'
                print(error_msg)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error_msg)
                    f.write('\n')

        else:
            ret_val = False
            
    return ret_val

# US08	Birth before marriage of parents
def us08_birth_before_marriage_of_parents(Individual, Family):
    error_msg = ''
    ret_val = False
    for i in Family:
        #print(i)
        if (i[1] != '' and i[2] ==''):
            #print(i[5])
            arr_of_children = i[5].split(' ')
            #print(arr_of_children)
            if(len(arr_of_children) > 0):
                for child in arr_of_children:
                    for inds in Individual:
                        if(inds[0] == child):
                            #print('same person', inds[0], child, inds)
                            if(i[1] > inds[3]):
                                error_msg = 'Anomaly US08: ' + \
                                    inds[1].replace(
                                        '/', '') + ' is born before the marriage of their parents'
                                ret_val = True
                                print(error_msg)
                                with open('gedcom_output.txt', 'a') as f:
                                    f.write(error_msg)
                                    f.write('\n')
                                
        elif (i[1] != '' and i[2] !=''): # and i[2] > i[1]):
            #print(i)
            arr_of_children = i[5].split(' ')
            #print(arr_of_children)
            if(len(arr_of_children) > 0):
                for child in arr_of_children:
                    for inds in Individual:
                        if(inds[0] == child):
                            print('same person', inds[0], child, inds)
                            num_months = (inds[3].year - i[2].year) * 12 + (inds[3].month - i[2].month)
                            print(i[2], inds[3], num_months)
                            if(i[2] < inds[3] and num_months < 9):
                                error_msg = 'Anomaly US08: ' + \
                                    inds[1].replace(
                                        '/', '') + ' is born after the divorce of their parents'
                                ret_val = True
                                print(error_msg)
                                with open('gedcom_output.txt', 'a') as f:
                                    f.write(error_msg)
                                    f.write('\n')
                                
        else:
            ret_val = False
            
    return ret_val
