from .api import countryLevelData, admin1LevelData, admin2LevelData
from .utils import load_ISO3166_data, countryToISO3166_A3, ISO3166_A3ToCountry

__version__ = "0.1.0"
__author__ = "Human Geomonitor"
__email__ = "david.gerard.23@ucl.ac.uk"


__all__ = ['countryLevelData', 
           'admin1LevelData', 
           'admin2LevelData',
           'load_ISO3166_data', 
           'countryToISO3166_A3', 
           'ISO3166_A3ToCountry']
