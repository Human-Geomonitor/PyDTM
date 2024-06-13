import unittest
from pydtm.api import countryLevelData, admin1LevelData, admin2LevelData

class TestAPIFunctions(unittest.TestCase):
    
    def test_countryLevelData(self):
        # Test case 1: Valid parameters
        response = countryLevelData(admin0Pcode="YEM", monthFrom_month="01", monthFrom_year=2000, monthTo_month="06", monthTo_year=2022)
        self.assertEqual(response['statusCode'], 200)
        
        # Test case 2: Invalid parameters (missing required parameter)
        with self.assertRaises(ValueError):
            countryLevelData(monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022)
        
        # Test case 3: Invalid parameters (both countryName and admin0Pcode provided)
        with self.assertRaises(ValueError):
            countryLevelData(countryName="Yemen", admin0Pcode="YEM", monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022)
        
        # Test case 4: No data found
        with self.assertRaises(ValueError):
            countryLevelData(admin0Pcode="RUS", monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022, to_pandas=True)
    
    def test_admin1LevelData(self):
        # Test case 1: Valid parameters
        response = admin1LevelData(admin0Pcode="YEM", monthFrom_month="01", monthFrom_year=2000, monthTo_month="06", monthTo_year=2022)
        self.assertEqual(response['statusCode'], 200)
        
        # Test case 2: Invalid parameters (missing required parameter)
        with self.assertRaises(ValueError):
            admin1LevelData(monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022)
        
        # Test case 3: Invalid parameters (both countryName and admin0Pcode provided)
        with self.assertRaises(ValueError):
            admin1LevelData(countryName="United States", admin0Pcode="USA", monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022)
        
        # Test case 4: No data found
        with self.assertRaises(ValueError):
            admin1LevelData(countryName="Canada", monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022, to_pandas=True)
    
    def test_admin2LevelData(self):
        # Test case 1: Valid parameters
        response = admin2LevelData(admin0Pcode="YEM", monthFrom_month="01", monthFrom_year=2000, monthTo_month="06", monthTo_year=2022)
        self.assertEqual(response['statusCode'], 200)
        
        # Test case 2: Invalid parameters (missing required parameter)
        with self.assertRaises(ValueError):
            admin2LevelData(monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022)
        
        # Test case 3: Invalid parameters (both countryName and admin0Pcode provided)
        with self.assertRaises(ValueError):
            admin2LevelData(countryName="United States", admin0Pcode="USA", monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022)
        
        # Test case 4: No data found
        with self.assertRaises(ValueError):
            admin2LevelData(countryName="Canada", monthFrom_month="01", monthFrom_year=2022, monthTo_month="06", monthTo_year=2022, to_pandas=True)

if __name__ == '__main__':
    unittest.main()