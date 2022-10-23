from gedcom import *

#US15 Fewer than 15 siblings: There should be fewer than 15 siblings in a family
def us15_fewer_than_15_siblings(Family):
    eval = True

    for i in Family:
        children_id = i[5].split()
        family_id = i[0]

        count = 0

        for c in children_id:
            count+=1

        if (count >= 15):
            error = 'Error US15: Family (' + family_id + ') has 15 or more siblings.'
            print(error)
            eval = False
            with open('gedcom_output.txt', 'a') as f:
                f.write(error)
                f.write('\n')
                f.close()

    return eval

#US13 Sibling spacing: Birth dates of siblings should be more than 8 months
#apart or less than 2 days apart (twins may be born one day apart,
#e.g. 11:59 PM and 12:02 AM the following calendar day)
def us13_sibling_spacing(Individual, Family):
    eval = True
    #sibling_1_birthday ='#'
    #sibling_2_birthday =''

    for i in Family:
        children_id = i[5].split()

        c = children_id[0]

        for k in Individual:
            if(c == k[0]):
                sibling_1_birthday = k[3]
                sibling_1_name = k[1].replace('/',"")
                sibling_1_id = k[0]

        for d in children_id:
            for l in Individual:
                if(c != d):
                    if(d == l[0]):
                        sibling_2_birthday = l[3]
                        sibling_2_name = l[1].replace('/',"")
                        sibling_2_id = l[0]

                        dif = abs((sibling_1_birthday.year-sibling_2_birthday.year)*12 + (sibling_1_birthday.month - sibling_2_birthday.month))
                        dif2 = abs((sibling_1_birthday-sibling_2_birthday).days)

                        #print(dif2)

                        if((dif < 8) and (dif2 > 2)):

                            error = ('Error US13: Birthdays of siblings '+sibling_1_name+' ('+sibling_1_id+') and '+sibling_2_name+' ('+sibling_2_id+') are between 2 days and 8 months apart')
                            print(error)
                            eval = False
                            with open('gedcom_output.txt', 'a') as f:
                                f.write(error)
                                f.write('\n')
                                f.close()

    return eval
