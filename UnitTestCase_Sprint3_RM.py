import unittest
from gedcom import *
from UserStories_Sprint3_RM import *


class ged_com_unit_test(unittest.TestCase):

    ########################################
    # US10: Marriage after 14
    ########################################

    def test_us10_01(self):

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

        ret_val = us10_Marriage_before_14(dfi, dff)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)

    ########################################
    # US14: Multiple births <= 5
    ########################################

    def test_us14_01(self):

        birthday_husband = dt.date(1975, 1, 10)
        birthday_wife = dt.date(1976, 1, 10)

        deathdate_husband = 'NA'
        alive_husband = True
        deathdate_wife = 'NA'
        alive_wife = True

        marriage_date = dt.date(1980, 12, 22)
        divorce_date = dt.date(2005, 12, 22)

        dfi = pd.DataFrame(
            columns=['ID', 'Name', 'Gender', 'Birthday', 'Alive', 'Death', 'Child'])
        dfi.loc[0] = ['I100', 'Rancho Chanchad', 'M',
                      birthday_husband, alive_husband, deathdate_husband, 'NA']
        dfi.loc[1] = ['I101', 'Priya Chanchad', 'F',
                      birthday_wife, alive_wife, deathdate_wife, 'NA']

        dfi.loc[2] = ['I102', 'One Chanchad', 'M',
                      dt.date(2000, 12, 22), True, 'NA', "{'F100'}"]
        dfi.loc[3] = ['I103', 'Two Chanchad', 'F',
                      dt.date(2000, 12, 22), True, 'NA', "{'F100'}"]
        dfi.loc[4] = ['I104', 'Three Chanchad', 'M',
                      dt.date(2000, 12, 22), True, 'NA', "{'F100'}"]
        dfi.loc[5] = ['I105', 'Four Chanchad', 'F',
                      dt.date(2000, 12, 22), True, 'NA', "{'F100'}"]
        dfi.loc[6] = ['I106', 'Five Chanchad', 'F',
                      dt.date(2000, 12, 22), True, 'NA', "{'F100'}"]
        dfi.loc[7] = ['I107', 'Six Chanchad', 'F',
                      dt.date(2000, 12, 22), True, 'NA', "{'F100'}"]

        dff = pd.DataFrame(columns=['ID', 'Married', 'Divorced',
                           'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name'])
        dff.loc[0] = ['F100', marriage_date, divorce_date,
                      'I100', 'Rancho Chanchad', 'I101', 'Priya Chanchad']

        ret_val = us14_Multiple_Births(dfi, dff)

        message = "Test value is not false."

        self.assertFalse(ret_val, message)


if __name__ == '__main__':
    # create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
