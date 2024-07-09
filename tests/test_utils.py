import unittest

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.pydtm.utils import load_ISO3166_data, countryToISO3166_A3, ISO3166_A3ToCountry


class TestAPIFunctions(unittest.TestCase):
    
    def test_load_ISO3166_data(self):
        # Test case 1: Check that loading data doesn't raise an exception
        load_ISO3166_data()
        
    
    def test_countryToISO3166_A3(self):
        # Test case 1: Valid parameters
        self.assertEqual(countryToISO3166_A3("Yemen"),"YEM")
        
    
    def test_ISO3166_A3ToCountry(self):
        # Test case 1: Valid parameters
        self.assertEqual(ISO3166_A3ToCountry("YEM"),"Yemen")

if __name__ == '__main__':
    unittest.main()