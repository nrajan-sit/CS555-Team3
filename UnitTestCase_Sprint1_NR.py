import unittest
from gedcom import *
from user_stories_sprint_1 import *

class ged_com_unit_test(unittest.TestCase):
    
    ########################################
    ## US03
    ########################################
    # Test_case_1
    def test_us03_01(self):
        
        test_ind = []
        ind_id = 'I100'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = '2010-01-01'
        ind_dod = '2009-01-01'
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])
        ret_val = us03_birth_before_death(test_ind)
    
        #print(test_ind)
        #print('answer = ', ret_val)
        
        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us03_02(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Steven Philip'
        ind_sex = 'M'
        ind_dob = '2010-01-01'
        ind_dod = '2019-01-01'
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])
        ret_val = us03_birth_before_death(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us03_03(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'James Bond'
        ind_sex = 'M'
        ind_dob = '2010-01-01'
        ind_dod = '2010-01-01'
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])
        ret_val = us03_birth_before_death(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)
        
    # Test_case_4
    def test_us03_04(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Captain Marvel'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = '2019-01-01'
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us03_birth_before_death(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        self.assertIs(ret_val, True)
        
    # Test_case_5
    def test_us03_05(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Carol Baskins'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = '2009-01-01'
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        ret_val = us03_birth_before_death(test_ind)

        #print(test_ind)
        #print('answer = ', ret_val)

        self.assertIsNot(ret_val, True)

    ########################################
    ## US04
    ########################################
    # Test_case_1
    def test_us04_01(self):

        test_fam = []
        fam_id = 'F100'
        marr_date = '2010-01-01'
        div_date = '2009-01-01'
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us04_marriage_before_divorce(test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us04_02(self):

        test_fam = []
        fam_id = 'F200'
        marr_date = '2010-01-01'
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        div_date = '2019-01-01'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us04_marriage_before_divorce(test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us04_03(self):

        test_fam = []
        fam_id = 'F300'
        marr_date = '2010-01-01'
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = ''
        div_date = ''
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us04_marriage_before_divorce(test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_4
    def test_us04_04(self):

        test_fam = []
        fam_id = 'F400'
        marr_date = '2010-01-01'
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        div_date = '2019-01-01'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us04_marriage_before_divorce(test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        self.assertIs(ret_val, True)

    # Test_case_5
    def test_us04_05(self):

        test_fam = []
        fam_id = 'F500'
        marr_date = '2020-01-01'
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I103'
        div_date = '2019-01-01'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        ret_val = us04_marriage_before_divorce(test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        self.assertIsNot(ret_val, True)
        
        
if __name__ == '__main__':
    #create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')
        
    unittest.main()
