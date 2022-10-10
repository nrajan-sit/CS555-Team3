import unittest
from gedcom import *
from Team_Sprint1 import *
from UserStories_Sprint2_NR import *
import datetime

class ged_com_unit_test(unittest.TestCase):

    ########################################
    ## US07
    ########################################
    # Test_case_1
    def test_us07_01(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = datetime.datetime(1900,1,1)
        ind_dod = datetime.datetime(2009,1,1)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us07_less_than_150yrs(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us07_02(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Steven Philip'
        ind_sex = 'M'
        ind_dob = datetime.datetime(1810,1,1)
        ind_dod = datetime.datetime(2019,1,1)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us07_less_than_150yrs(test_ind)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us07_03(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'James Bond'
        ind_sex = 'M'
        ind_dob = datetime.datetime(1850,1,1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us07_less_than_150yrs(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_4
    def test_us07_04(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Captain Marvel'
        ind_sex = 'F'
        ind_dob = datetime.datetime(1800,1,1)
        ind_dod = datetime.datetime(1951,1,1)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us07_less_than_150yrs(test_ind)

        # print(test_ind)
        # print('answer = ', ret_val)

        self.assertIs(ret_val, True)

    # Test_case_5
    def test_us07_05(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Carol Baskins'
        ind_sex = 'F'
        ind_dob = datetime.datetime(2000,1,1)
        ind_dod = datetime.datetime(2009,1,1)
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us07_less_than_150yrs(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        self.assertIsNot(ret_val, True)

    ########################################
    ## US08
    ########################################
    # Test_case_1
    def test_us08_01(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Captain Marvel'
        ind_sex = 'F'
        ind_dob = datetime.datetime(2000, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = datetime.datetime(1990,1,1)
        div_date = ''
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us08_birth_before_marriage_of_parents(test_ind, test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us04_02(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Steve Rogers'
        ind_sex = 'F'
        ind_dob = datetime.datetime(2000, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = datetime.datetime(2001, 1, 1)
        div_date = ''
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us08_birth_before_marriage_of_parents(test_ind, test_fam)

        # print(test_ind)
        # print(test_fam)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us04_03(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Tony Stark'
        ind_sex = 'M'
        ind_dob = datetime.datetime(2002, 8, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = datetime.datetime(2001, 1, 1)
        div_date = datetime.datetime(2002, 1, 1)
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us08_birth_before_marriage_of_parents(test_ind, test_fam)

        print(test_fam)
        print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_4
    def test_us04_04(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Tony Stark'
        ind_sex = 'M'
        ind_dob = datetime.datetime(2002, 12, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = datetime.datetime(2001, 1, 1)
        div_date = datetime.datetime(2002, 1, 1)
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us08_birth_before_marriage_of_parents(test_ind, test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        self.assertIs(ret_val, False)

    # Test_case_5
    def test_us04_05(self):

        test_ind = []
        ind_id = 'I103'
        ind_name = 'Tony Stark'
        ind_sex = 'M'
        ind_dob = datetime.datetime(2002, 12, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = datetime.datetime(2001, 1, 1)
        div_date = datetime.datetime(2003, 1, 1)
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us08_birth_before_marriage_of_parents(test_ind, test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        self.assertIsNot(ret_val, True)


if __name__ == '__main__':
    #create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
