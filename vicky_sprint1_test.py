import unittest
from gedcom import *

from Vicky_Sprint1_user_stories import birth_before_parents_death, parents_too_old

file_path = '/Users/Vicky/Desktop/gedcom_sprint_1.txt'

inds = gedcom_file_parser_ind(file_path)
fam = gedcom_file_parser_fam(file_path)

#print(inds[2][4])
#birth_before_parents_death(inds,fam)
parents_too_old(inds,fam)

#class testBirthBeforeParentsDeath(unittesti.TestCase)
#    def test_Birth_before_Parents_Death1(self):
