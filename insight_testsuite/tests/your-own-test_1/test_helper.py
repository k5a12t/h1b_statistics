import unittest
from shutil import copyfile
copyfile('../../../src/helper.py', 'helper.py')
from helper import *
from os import listdir


# copy generated output files to test directory
copyfile('../../../output/top_10_occupations.txt', 'output/top_10_occupations.txt')
copyfile('../../../output/top_10_states.txt', 'output/top_10_states.txt')


class CountingTestCase(unittest.TestCase):

    # test that the number of total certified applications is 0 or more
    def test_total_certified_is_zero_or_more(self):
        self.assertTrue(get_total_certified('input/h1b_input.csv') >= 0)
        #self.assertTrue(get_total_certified('input/H1B_FY_2014.csv') >= 0)

    # test that the number of total certified applications is an integer
    def test_total_certified_is_integer(self):
        self.assertTrue(isinstance(get_total_certified('input/h1b_input.csv'), int))
        #self.assertTrue(isinstance(get_total_certified('input/H1B_FY_2014.csv'), int))
    
    # test that the column number corresponding to status column is 0 or more
    def test_status_col_num_is_zero_or_more(self):
        self.assertTrue(get_status_col_num('input/h1b_input.csv') >= 0)
        #self.assertTrue(get_status_col_num('input/H1B_FY_2014.csv') >= 0)

    # test that the column number corresponding to status column is an integer
    def test_status_col_num_is_integer(self):
        self.assertTrue(isinstance(get_status_col_num('input/h1b_input.csv'), int))
        #self.assertTrue(isinstance(get_status_col_num('input/H1B_FY_2014.csv'), int))
    
    # test that the column number corresponding to occupation column is 0 or more
    def test_occupation_col_num_is_zero_or_more(self):
        self.assertTrue(get_occupation_col_num('input/h1b_input.csv') >= 0)
        #self.assertTrue(get_occupation_col_num('input/H1B_FY_2014.csv') >= 0)
    
    # test that the column number corresponding to occupation column is an integer
    def test_occupation_col_num_is_integer(self):
        self.assertTrue(isinstance(get_occupation_col_num('input/h1b_input.csv'), int))
        #self.assertTrue(isinstance(get_occupation_col_num('input/H1B_FY_2014.csv'), int))

    # test that the column number corresponding to state column is 0 or more
    def test_state_col_num_is_zero_or_more(self):
        self.assertTrue(get_state_col_num('input/h1b_input.csv') >= 0)
        #self.assertTrue(get_state_col_num('input/H1B_FY_2014.csv') >= 0)
    
    # test that the column number corresponding to state column is an integer
    def test_state_col_num_is_integer(self):
        self.assertTrue(isinstance(get_state_col_num('input/h1b_input.csv'), int))
        #self.assertTrue(isinstance(get_state_col_num('input/H1B_FY_2014.csv'), int))

    # test that the output directory has two files, top_10_occupations.txt & top_10_states.txt
    def test_output_files_present(self):
        self.assertTrue(listdir('output') == ['top_10_occupations.txt', 'top_10_states.txt'])

    # test that the output file top_10_occupations.txt has at most 11 lines (10 records + 1 header)
    def test_top_10_occupations_num_lines(self):
        f = open('output/top_10_occupations.txt')
        self.assertTrue(sum(1 for line in f) <= 11)
        f.close()

    # test that the output file top_10_states.txt has at most 11 lines (10 records + 1 header)
    def test_top_10_states_num_lines(self):
        f = open('output/top_10_states.txt')
        self.assertTrue(sum(1 for line in f) <= 11)
        f.close()

    # test that the header of top_10_occupations.txt matches the specifications
    def test_top_10_occupations_header_equal(self):
        f = open('output/top_10_occupations.txt')
        self.assertEqual(f.readline(), 'TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        f.close()

    # test that the header of top_10_states.txt matches the specifications
    def test_top_10_states_header_equal(self):
        f = open('output/top_10_states.txt')
        self.assertEqual(f.readline(), 'TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        f.close()

    # test that all lines in top_10_occupations.txt have 3 fields, separated by a ;
    def test_top_10_occupations_num_fields_equal(self):
        f = open('output/top_10_occupations.txt')
        for line in f:
            fields = line.split(';')
            self.assertTrue(len(fields) == 3)
        f.close()

    # test that all lines in top_10_states.txt have 3 fields, separated by a ;
    def test_top_10_states_num_fields_equal(self):
        f = open('output/top_10_states.txt')
        for line in f:
            fields = line.split(';')
            self.assertTrue(len(fields) == 3)
        f.close()


if __name__ == '__main__':
    unittest.main()

