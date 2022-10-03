from Vicky_Sprint1_user_stories import *
from gedcom import *
import unittest


#file_path = '/Users/Vicky/Desktop/gedcom_sprint_1.txt'

#inds = gedcom_file_parser_ind(file_path)
#fam = gedcom_file_parser_fam(file_path)

#US09 Birth before parents' Death
#birth_before_parents_death(inds, fam)

#US12 parents not too old (mother less than 60 years older and father less than 80 years older than children)
#parents_too_old(inds, fam)

###Testing US09
class TestBirthBeforeParentsDeath(unittest.TestCase):
#testcase 1
    def test_Birth_before_Parents_Death_01(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = '1988-01-01'
        ind_dod02 = '2009-01-01'
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = '1989-01-01'
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = birth_before_parents_death(test_inds, test_fam)

        expected = False

        self.assertEqual(actual, expected)


#testcase 2
    def test_Birth_before_Parents_Death_02(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = '1988-01-01'
        ind_dod02 = '2009-01-01'
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = '1989-01-01'
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = birth_before_parents_death(test_inds, test_fam)

        self.assertFalse(actual)


#TestCase 3
    def test_Birth_before_Parents_Death_03(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = '1988-01-01'
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = '1989-01-01'
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = birth_before_parents_death(test_inds, test_fam)

        self.assertTrue(actual)


#TestCase 4
    def test_Birth_before_Parents_Death_04(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = '1988-01-01'
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = '1989-01-01'
        ind_dod03 = '2000-4-20'
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = birth_before_parents_death(test_inds, test_fam)

        self.assertFalse(actual)

#TestCase 5
    def test_Birth_before_Parents_Death_05(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = '2010-01-01'
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = '1988-01-01'
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = '1989-01-01'
        ind_dod03 = '2000-4-20'
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = birth_before_parents_death(test_inds, test_fam)
        Expected = False

        self.assertEqual(actual, Expected)

###Testing US12
class TestParentsTooOld(unittest.TestCase):
#testcase 1
    def test_Parents_Too_Old_01(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('2010-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('1988-01-01', '%Y-%m-%d').date()
        ind_dod02 = datetime.strptime('2009-01-01', '%Y-%m-%d').date()
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('1989-01-01', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = parents_too_old(test_inds, test_fam)

        expected = True

        self.assertEqual(actual, expected)


#testcase 2
    def test_Parents_Too_Old_02(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('2010-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('1988-01-01', '%Y-%m-%d').date()
        ind_dod02 = datetime.strptime('2009-01-01', '%Y-%m-%d').date()
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('1989-01-01', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = parents_too_old(test_inds, test_fam)

        self.assertTrue(actual)


#TestCase 3
    def test_Parents_Too_Old_03(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('2010-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('1989-01-01', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = parents_too_old(test_inds, test_fam)

        self.assertFalse(actual)


#TestCase 4
    def test_Parents_Too_Old_04(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('2010-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('1988-01-01', '%Y-%m-%d').date()
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = parents_too_old(test_inds, test_fam)

        self.assertFalse(actual)

#TestCase 5
    def test_Parents_Too_Old_05(self):

        test_inds = []
        ind_id = 'I10'
        ind_name = 'Lucy Hale'
        ind_sex = 'F'
        ind_dob = datetime.strptime('2010-01-01', '%Y-%m-%d').date()
        ind_dod = ''
        ind_famc = 'F1'
        ind_fams = ''
        test_inds.append([ind_id, ind_name, ind_sex, ind_dob, ind_dod, ind_famc, ind_fams])

        ind_id02 = 'I9'
        ind_name02 = 'William Hale'
        ind_sex02 = 'M'
        ind_dob02 = datetime.strptime('1988-01-01', '%Y-%m-%d').date()
        ind_dod02 = ''
        ind_famc02 = ''
        ind_fams02 = 'F1'
        test_inds.append([ind_id02, ind_name02, ind_sex02, ind_dob02, ind_dod02, ind_famc02, ind_fams02])

        ind_id03 = 'I8'
        ind_name03 = 'Lina Hale'
        ind_sex03 = 'F'
        ind_dob03 = datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        ind_dod03 = ''
        ind_famc03 = ''
        ind_fams03 = 'F1'
        test_inds.append([ind_id03, ind_name03, ind_sex03, ind_dob03, ind_dod03, ind_famc03, ind_fams03])

        test_fam = []
        fam_id = 'F1'
        marr_date = ''
        div_date = ''
        hus_id = 'I9'
        wife_id = 'I8'
        child_id = 'I10'

        test_fam.append([fam_id, marr_date, div_date, hus_id, wife_id,
                        child_id])

        actual = parents_too_old(test_inds, test_fam)
        Expected = False

        self.assertEqual(actual, Expected)


#Main Method
if __name__ == '__main__':
    #create output file
    with open('gedcom_output.txt', 'w') as f:
        f.write('')

    unittest.main()
