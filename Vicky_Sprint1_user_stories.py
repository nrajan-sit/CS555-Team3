from gedcom import *
from datetime import datetime


#US09 Birth before parents' Death
def birth_before_parents_death(Individual, Family):

    parent1_death = ''
    parent2_death = ''
    child_birth = ''
    child_name = ''
    eval = True

    for i in Family:
        for j in Individual:
            if (i[3] == j[0]):
                parent1_death = j[4]


            if (i[4] == j[0]):
                parent2_death = j[4]


        children_id = i[5].split()

        if(parent1_death != ''):
            for c in children_id:
                for d in Individual:
                    if (c == d[0]):
                        child_birth = d[3]
                        child_name = d[1].replace('/',"")

                        if (parent1_death <= child_birth):
                            print("Error US09: Birthday of " + child_name + " occurs after his/her father's death")
                            eval = False

        if(parent2_death != ''):
            for c in children_id:
                for d in Individual:
                    if (c == d[0]):
                        child_birth = d[3]
                        child_name = d[1].replace('/',"")

                        if (parent2_death <= child_birth):
                            print("Error US09: Birthday of " + child_name + " occurs after his/her mother's death")
                            eval = False




#US12 parents not too old (mother less than 60 years older and father less than 80 years older than children)
def parents_too_old(Individual, Family):

    husband_birth = ''
    wife_birth = ''
    child_birth = ''
    child_name = ''
    eval = True


    for i in Family:
        for j in Individual:
            if (i[3] == j[0]):
                husband_birth = j[3]
                husband_birth_int = husband_birth.year + husband_birth.month+husband_birth.day


            if (i[4] == j[0]):
                wife_birth = j[3]
                wife_birth_int = wife_birth.year + wife_birth.month +wife_birth.day
                #print(wife_birth_int)


        children_id = i[5].split()

        for c in children_id:
            for d in Individual:
                if (c == d[0]):
                    child_birth = d[3]
                    child_birth_int = child_birth.year + child_birth.month+ child_birth.day
                    #print(child_birth_int)
                    child_name = d[1].replace('/',"")
                    difference = child_birth_int - husband_birth_int

                    if (difference >= 80):
                        print("Anomaly US12: Father of " + child_name + " 80 years older than child")
                        eval = False


        for c in children_id:
            for d in Individual:
                if (c == d[0]):
                    child_birth = d[3]
                    child_birth_int = child_birth.year + child_birth.month+ child_birth.day
                    child_name = d[1].replace('/',"")
                    difference = child_birth_int - wife_birth_int

                    if (difference >= 60):
                        print("Anomaly US12: Mother of " + child_name + " 60 years older than child")
                        eval = False