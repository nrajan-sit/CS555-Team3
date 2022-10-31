import unittest
from gedcom import *
from Team_Sprint1 import *
from UserStories_Sprint4_NR import *
from datetime import date


class ged_com_unit_test(unittest.TestCase):

    ########################################
    ## US36
    ########################################
    # Test_case_1
    def test_us36_01(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = date(1900, 1, 1)
        ind_dod = date(2022, 9, 1)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us36_list_recent_deaths(test_ind)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us36_02(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Steven Philip'
        ind_sex = 'M'
        ind_dob = date(1810, 1, 1)
        ind_dod = date(2022, 10, 10)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us36_list_recent_deaths(test_ind)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us36_03(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'James Bond'
        ind_sex = 'M'
        ind_dob = date(1850, 1, 1)
        ind_dod = date(2022, 10, 10)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us36_list_recent_deaths(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    ########################################
    ## US38
    ########################################
    # Test_case_1
    def test_us38_01(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Captain Marvel'
        ind_sex = 'F'
        ind_dob = date(2000, 10, 3)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ret_val = us38_list_upcoming_birthdays(test_ind)

        #print(test_fam)
        #print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us38_02(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Steve Rogers'
        ind_sex = 'F'
        ind_dob = date(2000, 10, 20)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ret_val = us38_list_upcoming_birthdays(test_ind)

        # print(test_ind)
        # print(test_fam)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us38_03(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Tony Stark'
        ind_sex = 'M'
        ind_dob = date(2002, 10, 15)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ret_val = us38_list_upcoming_birthdays(test_ind)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)


if __name__ == '__main__':
    #create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
