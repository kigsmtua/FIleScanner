#Test cases for the weather file reader application

import unittest
from weather import *

class CalculateWeatherTests(unittest.TestCase):

    def test_error_is_thrown_for_wrong_file(self):
        with self.assertRaises(IOError,msg="IOError occured while reading file"):
            read_data_from_file('main.dat')

    def test_values_are_cleaned_for_calculation(self):
        result = clean_mnt_or_mxt_value("37*")
        self.assertEqual(result,37.0,"Should return 37.0 from 37*")

    def test_spread_values_are_calculated_correctly(self):
        values = [['0','43','3'],['0','2','3']]
        result = calculate_spreads(values)
        self.assertEqual(result,{'0': 40.0},"Should return dictionary with values '0' and 40")

    def  test_maximum_value_is_what_is_picked(self):
        values = {'9':54.0,'18':53.0}
        result = get_max_spread_value(values)
        self.assertEqual(result,"Day : 9 Spread: 54.0","Should output 54")

##Runs the test cases for the application
if __name__ == '__main__':
    unittest.main()
