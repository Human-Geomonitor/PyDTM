import unittest
from pydtm.utils import load_ISO3166_data, countryToISO3166_A3, ISO3166_A3ToCountry


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