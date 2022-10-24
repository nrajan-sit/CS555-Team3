from gedcom import *

#US31 List Living Single: List all living people over 30 who have never been
#married in a GEDCOM file
def us31_list_living_single(Individual):
    living_single_name = []
    living_single_id = []
    eval = False

    for i in Individual:
        if (i[4] == ''):
            person_id = i[0]
            person_name = i[1].replace('/',"")
            person_birthday = i[3]

            today = date.today()
            person_age = today.year - person_birthday.year - ((today.month, today.day) < (person_birthday.month, person_birthday.day))

            if(person_age > 30):
                if (i[6] == ''):
                    living_single_name.append(person_name)
                    living_single_id.append(person_id)
                    eval = True

    opening_sentence = ('US31: These individuals are alive, over 30 and never been married: ')
    print(opening_sentence, end = "")
    with open('gedcom_output.txt', 'a') as f:
        f.write(opening_sentence)

    for j,k in zip(living_single_name, living_single_id):
        print(j+'('+k+') ', end = "")
        with open('gedcom_output.txt', 'a') as f:
            f.write(j+' ('+k+') ')

    print('.')
    with open('gedcom_output.txt', 'a') as f:
        f.write('.\n')

    return eval

#US30 List Living Married: List all living married people in a GEDCOM file
def us30_list_living_married(Individual, Family):
    living_married_name = []
    living_married_id = []
    eval = False

    for i in Individual:
        if (i[4] == ''):
            person_id = i[0]
            person_name = i[1].replace('/',"")

            if (i[6] != ''):
                spouses = i[6].split()

                for s in spouses:
                    for f in Family:
                        if ((s == f[0]) and (f[2] == '')):

                            if(person_id == f[3]):
                                for m in Individual:
                                    if((f[4] == m[0]) and (m[4] == '')):
                                        eval = True
                                        living_married_name.append(person_name)
                                        living_married_id.append(person_id)

                            if(person_id == f[4]):
                                for n in Individual:
                                    if((f[3] == n[0]) and (n[4] == '')):
                                        eval = True
                                        living_married_name.append(person_name)
                                        living_married_id.append(person_id)

    opening_sentence = ('US30: These individuals are alive and married: ')
    print(opening_sentence, end = "")
    with open('gedcom_output.txt', 'a') as f:
        f.write(opening_sentence)

    for j,k in zip(living_married_name, living_married_id):
        print(j+'('+k+') ', end = "")
        with open('gedcom_output.txt', 'a') as f:
            f.write(j+' ('+k+') ')

    print('.')
    with open('gedcom_output.txt', 'a') as f:
        f.write('.\n')

    return eval
