from UserStories_Sprint3_VT import *

#from gedcom import *
import unittest

#US15 Fewer than 15 siblings
class TestFewerThan15Siblings(unittest.TestCase):
#testcase 1
    def test_us15_fewer_than_15_siblings_01(self):

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10 I7'
        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])


        fam_id_02 = 'F2'
        marr_date_02 = ''
        div_date_02 = ''
        hus_id_02 = 'I18'
        wife_id_02 = 'I19'
        child_id_02 = 'I100 I17 I15 I1 I2 I3 I4 I5 I6 I11 I12 I13 I14 I16 I20'

        test_fam.append([fam_id_02, marr_date_02, div_date_02, hus_id_02, wife_id_02,
                        child_id_02])

        actual = us15_fewer_than_15_siblings(test_fam)

        expected = False

        self.assertEqual(actual, expected)


#US13 Sibling spacing
class TestSiblingSpacing(unittest.TestCase):
#testcase 1
    def test_us13_sibling_spacing_01(self):
        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10 I7 I4 I5'
        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                    child_id])


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
        ind_dob02 = datetime.strptime('2010-03-01', '%Y-%m-%d').date()
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I4'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('2010-12-02', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        ind_id04 = 'I5'
        ind_name04 = 'Allison Hale'
        ind_sex04 = 'F'
        ind_dob04 = datetime.strptime('2009-12-31', '%Y-%m-%d').date()
        ind_dod04 = ''
        ind_famc04 = ''
        ind_fams04 = 'F1'
        test_inds.append([ind_id04, ind_name04, ind_sex04, ind_dob04, ind_dod04, ind_famc04, ind_fams04])

        actual = us13_sibling_spacing(test_inds, test_fam)

        expected = False

        self.assertEqual(actual, expected)



############## Main ####################################################
if __name__ == '__main__':
    # create output file
    #with open('gedcom_output.txt', 'w') as f:
        #f.write('')

    unittest.main()
