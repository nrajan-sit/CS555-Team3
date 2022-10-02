from gedcom import *

#US03 : Birth before death
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
    return ret_val

# US04 : Marriage before divorce
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
    return ret_val
