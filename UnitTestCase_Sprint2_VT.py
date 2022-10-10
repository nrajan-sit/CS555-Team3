from UserStories_Sprint2_VT import *
#from gedcom import *
import unittest


#US17 No marriage to descendants
class TestNoMarriageToDescendants(unittest.TestCase):
#testcase 1
    def test_us17_no_marriage_to_descendants_01(self):

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I10'
        child_id = 'I10 I7 I5'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        fam_id_02 = 'F2'
        marr_date_02 = ''
        div_date_02 = ''
        hus_id_02 = 'I17'
        wife_id_02 = 'I19'
        child_id_02 = 'I100 I17 I15'

        test_fam.append([fam_id_02, marr_date_02, div_date_02, hus_id_02, wife_id_02,
                        child_id_02])

        actual = us17_no_marriage_to_descendants(test_fam)

        expected = False

        self.assertEqual(actual, expected)


#US18 siblings should not marry
class TestNoMarriageBetweenSiblings(unittest.TestCase):
#testcase 1
    def test_No_Marriage_between_Siblings_01(self):


        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I3'
        wife_id = 'I4'
        child_id = 'I9 I8'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])


        fam_id_02 = 'F2'
        marr_date_02 = ''
        div_date_02 = ''
        hus_id_02 = 'I9'
        wife_id_02 = 'I8'
        child_id_02 = ''

        test_fam.append([fam_id_02, marr_date_02, div_date_02, hus_id_02, wife_id_02,
                        child_id_02])

        actual = us18_no_marriage_between_siblings(test_fam)

        expected = False

        self.assertEqual(actual, expected)

############## Main ####################################################
if __name__ == '__main__':
    # create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
