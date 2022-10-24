from UserStories_Sprint4_VT import *

#from gedcom import *
import unittest

#US31 List Living Single
class TestListLivingSingle(unittest.TestCase):
#testcase 1
    def test_us31_list_living_single_01(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('1988-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I7'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('2058-03-01', '%Y-%m-%d').date()
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I4'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('2061-12-02', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        actual = us31_list_living_single(test_inds)

        expected = True

        self.assertEqual(actual, expected)

#US30 List Living Married
class TestListLivingMarried(unittest.TestCase):
#testcase 1
    def test_us30_list_living_married_01(self):

        test_inds = []

        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('2010-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I7'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('1980-03-01', '%Y-%m-%d').date()
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1 F2'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I4'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('1982-12-02', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1 F3'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        ind_id04 = 'I5'
        ind_name04 = 'Allison Hale'
        ind_sex04 = 'F'
        ind_dob04 = datetime.strptime('1984-12-31', '%Y-%m-%d').date()
        ind_dod04 = ''
        ind_famc04 = ''
        ind_fams04 = 'F2'
        test_inds.append([ind_id04, ind_name04, ind_sex04, ind_dob04, ind_dod04, ind_famc04, ind_fams04])

        ind_id05 = 'I6'
        ind_name05 = 'Gale Hale'
        ind_sex05 = 'F'
        ind_dob05 = datetime.strptime('1984-12-31', '%Y-%m-%d').date()
        ind_dod05 = '2020-01-01'
        ind_famc05 = ''
        ind_fams05 = 'F3'
        test_inds.append([ind_id05, ind_name05, ind_sex05, ind_dob05, ind_dod05, ind_famc05, ind_fams05])

        test_fam = []
        fam_id = 'F1'
        marr_date = '2008-01-01'
        div_date = '2012-01-01'
        hus_id = 'I7'
        wife_id = 'I4'
        child_id = 'I10'
        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                    child_id])

        fam_id02 = 'F2'
        marr_date02 = '2015-01-01'
        div_date02 = ''
        hus_id02 = 'I7'
        wife_id02 = 'I5'
        child_id02 = ''
        test_fam.append([fam_id02, marr_date02, div_date02, hus_id02, wife_id02,
                    child_id02])

        fam_id03 = 'F3'
        marr_date03 = '2016-01-01'
        div_date03 = ''
        hus_id03 = 'I6'
        wife_id03 = 'I4'
        child_id03 = ''
        test_fam.append([fam_id03, marr_date03, div_date03, hus_id03, wife_id03,
                    child_id03])

        actual = us30_list_living_married(test_inds, test_fam)

        expected = True

        self.assertEqual(actual, expected)

############## Main ####################################################
if __name__ == '__main__':
    # create output file
    #with open('gedcom_output.txt', 'w') as f:
        #f.write('')

    unittest.main()
