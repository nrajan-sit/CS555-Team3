import unittest
from gedcom import *
from Team_Sprint1 import *
from UserStories_Sprint3_NR import *
from datetime import date


class ged_com_unit_test(unittest.TestCase):

    ########################################
    ## US16
    ########################################
    # Test_case_1
    def test_us16_01(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = date(1950, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        
        ind_id = 'I101'
        ind_name = 'Jenny Stevens'
        ind_sex = 'F'
        ind_dob = date(1955, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        
        ind_id = 'I102'
        ind_name = 'Joey S'
        ind_sex = 'M'
        ind_dob = date(1987, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        
        ind_id = 'I103'
        ind_name = 'Jennifer Stevens'
        ind_sex = 'F'
        ind_dob = date(1990, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])
        
        test_fam = []
        fam_id = 'F100'
        marr_date = date(1982, 1, 1)
        div_date = ''
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I102 I103 '
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])
        
        ret_val = us16_male_last_names(test_ind, test_fam)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us16_02(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = date(1950, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I101'
        ind_name = 'Jenny Stevens'
        ind_sex = 'F'
        ind_dob = date(1955, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I102'
        ind_name = 'Joey Stevens'
        ind_sex = 'M'
        ind_dob = date(1987, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I103'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = date(1990, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = date(1982, 1, 1)
        div_date = ''
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I102 I103 '
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])

        ret_val = us16_male_last_names(test_ind, test_fam)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us16_03(self):

        test_ind = []
        ind_id = 'I100'
        ind_name = 'Joseph Stevens'
        ind_sex = 'M'
        ind_dob = date(1950, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I101'
        ind_name = 'Jenny Stevens'
        ind_sex = 'F'
        ind_dob = date(1955, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I102'
        ind_name = 'Jessica S'
        ind_sex = 'F'
        ind_dob = date(1987, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I103'
        ind_name = 'Jennifer Stevens'
        ind_sex = 'F'
        ind_dob = date(1990, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = date(1982, 1, 1)
        div_date = ''
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I102 I103 '
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])

        ret_val = us16_male_last_names(test_ind, test_fam)
        #print(test_ind)
        #print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    ########################################
    ## US38
    ########################################
    # Test_case_1
    def test_us21_01(self):

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

        ind_id = 'I101'
        ind_name = 'Jenny Stevens'
        ind_sex = 'F'
        ind_dob = date(1900, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = date(2001, 1, 1)
        div_date = date(2002, 1, 1)
        hus_id = 'I101'
        wife_id = 'I100'
        child_id = 'I102'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])

        ret_val = us21_correct_gender_for_role(test_ind, test_fam)

        #print(test_fam)
        #print('answer = ', ret_val)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us21_02(self):

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

        ind_id = 'I101'
        ind_name = 'Jenny Stevens'
        ind_sex = 'F'
        ind_dob = date(1900, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        ind_id = 'I102'
        ind_name = 'Jessica Jenny'
        ind_sex = 'F'
        ind_dob = date(1990, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])

        test_fam = []
        fam_id = 'F100'
        marr_date = date(2001, 1, 1)
        div_date = date(2002, 1, 1)
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = 'I102'
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])

        ret_val = us21_correct_gender_for_role(test_ind, test_fam)

        # print(test_ind)
        # print(test_fam)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us21_03(self):

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

        ind_id = 'I101'
        ind_name = 'Jenny Stevens'
        ind_sex = 'F'
        ind_dob = date(1900, 1, 1)
        ind_dod = ''
        ind_famc = ''
        ind_fams = ''

        test_ind.append([ind_id, ind_name, ind_sex, ind_dob,
                        ind_dod, ind_famc, ind_fams])


        test_fam = []
        fam_id = 'F100'
        marr_date = date(2001, 1, 1)
        div_date = ''
        hus_id = 'I100'
        wife_id = 'I101'
        child_id = ''
        event_date = ''

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id, event_date])

        ret_val = us21_correct_gender_for_role(test_ind, test_fam)

        # print(test_ind)
        # print('answer = ', ret_val)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)


if __name__ == '__main__':
    #create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
