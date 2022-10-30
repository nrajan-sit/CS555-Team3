import unittest
from gedcom import *
from UserStories_Sprint4_RM import *


class ged_com_unit_test(unittest.TestCase):

    ########################################
    # US29: List deceased
    ########################################

    def test_us29_01(self):

        birthday_husband = dt.date(1975, 1, 10)
        birthday_wife = dt.date(1976, 1, 10)

        deathdate_husband = dt.date(2003, 1, 10)
        alive_husband = False
        deathdate_wife = 'NA'
        alive_wife = True

        marriage_date = dt.date(1980, 12, 22)
        divorce_date = dt.date(2005, 12, 22)

        dfi = pd.DataFrame(
            columns=['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death'])
        dfi.loc[0] = ['I100', 'Rancho Chanchad', 'M',
                      birthday_husband, alive_husband, deathdate_husband]
        dfi.loc[1] = ['I101', 'Priya Chanchad', 'F',
                      birthday_wife, alive_wife, deathdate_wife]

        dff = pd.DataFrame(columns=['ID', 'Married', 'Divorced',
                           'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name'])
        dff.loc[0] = ['F100', marriage_date, divorce_date,
                      'I100', 'Rancho Chanchad', 'I101', 'Priya Chanchad']

        ret_val = us29_List_Deceased(dfi, dff)

        message = "Test value is not True."

        self.assertTrue(ret_val, message)

    ########################################
    # US35: List recent births
    ########################################

    def test_us35_01(self):

        birthday_husband = dt.date(1975, 1, 10)
        birthday_wife = dt.date(2022, 10, 10)

        deathdate_husband = dt.date(2003, 1, 10)
        alive_husband = False
        deathdate_wife = 'NA'
        alive_wife = True

        marriage_date = dt.date(1980, 12, 22)
        divorce_date = dt.date(2005, 12, 22)

        dfi = pd.DataFrame(
            columns=['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death'])
        dfi.loc[0] = ['I100', 'Rancho Chanchad', 'M',
                      birthday_husband, alive_husband, deathdate_husband]
        dfi.loc[1] = ['I101', 'Priya Chanchad', 'F',
                      birthday_wife, alive_wife, deathdate_wife]

        dff = pd.DataFrame(columns=['ID', 'Married', 'Divorced',
                           'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name'])
        dff.loc[0] = ['F100', marriage_date, divorce_date,
                      'I100', 'Rancho Chanchad', 'I101', 'Priya Chanchad']

        ret_val = us35_List_Recent_Births(dfi, dff)

        message = "Test value is not True."

        self.assertTrue(ret_val, message)


if __name__ == '__main__':
    # create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
