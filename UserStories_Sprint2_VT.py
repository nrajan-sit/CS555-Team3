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
                error = 'Error US17: Husband (' + husband_id + ') of family ('+family_id +') is married to his child ('+c+').'
                print(error)
                eval = False
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error)
                    f.write('\n')
                    f.close()

            if (c == wife_id):
                error = 'Error US17: Wife (' + wife_id + ') of family ('+family_id +') is married to her child ('+c+').'
                print(error)
                eval = False
                with open('gedcom_output.txt', 'a') as f:
                    f.write(error)
                    f.write('\n')
                    f.close()

    return eval


#US18 siblings should not marry
def us18_no_marriage_between_siblings(Individual, Family):

    eval = True
    child_id = ''
    child_name = ''
    spouse = ''
    family = ''


    for i in Family:
        children_id = i[5].split()
        family = i[0]

        for c in children_id:
            for j in Individual:
                if (c == j[0]):
                    child_id = j[0];
                    spouse = j[6];
                    child_name = j[1].replace('/',"")
                    child_gender = ''
                    if (j[2] == 'M'):
                        child_gender = 'his'
                    if (j[2] == 'F'):
                        child_gender = 'her'

                    if (spouse == family):
                        anomaly = 'Anomaly US18: '+ child_name + ' ('+child_id+ ') is married to '+ child_gender + ' sibling in family ('+ family +').'
                        eval = False
                        print(anomaly)
                        with open('gedcom_output.txt', 'a') as f:
                            f.write(anomaly)
                            f.write('\n')
                            f.close()

    return eval
