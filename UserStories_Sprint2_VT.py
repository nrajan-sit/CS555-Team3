from gedcom import *



#US17 No marriage to descendants
def us17_no_marriage_to_descendants(Family):

    child_id = ''
    husband_id = ''
    wife_id =''
    family_id = ''
    eval = True

    for i in Family:
        children_id = i[5].split()
        family_id = i[0]
        husband_id = i[3]
        wife_id = i[4]

        for c in children_id:
            if (c == husband_id):
                error = 'Error US17: Wife (' + wife_id + ') of family ('+family_id +') is married to her child ('+c+').'
                print(error)
                eval = False
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error)
                    f.write('\n')
                    f.close()

            if (c == wife_id):
                error = 'Error US17: Husband (' + husband_id + ') of family ('+family_id +') is married to his child ('+c+').'
                print(error)
                eval = False
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error)
                    f.write('\n')
                    f.close()

    return eval


#US18 siblings should not marry
def us18_no_marriage_between_siblings(Family):

    eval = True
    husband_id = ''
    wife_id = ''
    husband_birth_family = ''
    wife_birth_family = ''
    marriage_family = ''

    for i in Family:
        husband_id = i[3]
        wife_id = i[4]
        marriage_family = i[0]

        for j in Family:
            if (j[5] != ''):
                children_id = j[5].split()

            for c in children_id:
                if (husband_id == c):
                    husband_birth_family = j[0]

                if(wife_id == c):
                    wife_birth_family = j[0]

            if(husband_birth_family == wife_birth_family):
                anomaly = 'Anomaly US18: Siblings from family (' + husband_birth_family +') are married to each other in family ('+ marriage_family+').'
                eval = False
                print(anomaly)
                with open('gedcom_output.txt', 'a') as f:
                    f.write(anomaly)
                    f.write('\n')
                    f.close()

    return eval
