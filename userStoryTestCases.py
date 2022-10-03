import unittest
from gedcom import *
from UserStories1and2 import *

class ged_com_unit_test(unittest.TestCase):
    
    ########################################
    ## US01: Dates before current date
    ########################################
    # Test_case_1
    def test_us01_01(self):

        birthday_husband = dt.date(2023,12,21)
        birthday_wife = dt.date(1980,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = dates_before_current(dfi,dff)
        
        message = "Test value is not false."

        self.assertFalse(ret_val, message)
    
    # Test_case_2
    def test_us01_02(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(1980,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = dates_before_current(dfi,dff)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_3
    def test_us01_03(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(1980,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = dates_before_current(dfi,dff)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)
        
    # Test_case_4
    def test_us01_04(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(1980,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = dates_before_current(dfi,dff)

        self.assertIs(ret_val, True)
        
    # Test_case_5
    def test_us01_05(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(2023,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = dates_before_current(dfi,dff)

        self.assertIsNot(ret_val, True)
    
    ########################################
    ## US02: Birth before marriage
    ########################################
    # Test_case_1
    def test_us02_01(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(2023,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,22)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = birth_before_marriage(dfi,dff)
        
        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_2
    def test_us02_02(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(2001,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(2000,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = birth_before_marriage(dfi,dff)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    # Test_case_3
    def test_us02_03(self):

        birthday_husband = dt.date(1998,12,21)
        birthday_wife = dt.date(1998,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(2000,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = birth_before_marriage(dfi,dff)

        message = "Test value is not true."

        self.assertTrue(ret_val, message)

    # Test_case_4
    def test_us02_04(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(2023,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(2023,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = birth_before_marriage(dfi,dff)

        self.assertIs(ret_val, True)

    # Test_case_5
    def test_us02_05(self):

        birthday_husband = dt.date(1980,12,21)
        birthday_wife = dt.date(2023,11,22)

        deathdate_husband = 'NA'
        deathdate_wife = 'NA'

        marriage_date = dt.date(1980,12,21)
        divorce_date = 'NA'
        
        dfi = pd.DataFrame( columns=['ID', 'Name', 'Gender', 'Birthday', 'Death'])
        dfi.loc[0] =['I100','Rancho Chanchad','M',birthday_husband,deathdate_husband]
        dfi.loc[1] =['I101','Priya Chanchad','F',birthday_wife,deathdate_wife]

        dff = pd.DataFrame( columns=['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID','Wife Name'])
        dff.loc[0] =['F100',marriage_date,divorce_date,'I100','Rancho Chanchad','I101','Priya Chanchad']

        
        ret_val = birth_before_marriage(dfi,dff)

        self.assertIsNot(ret_val, True)
    
        
if __name__ == '__main__':
    #create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
        
    
