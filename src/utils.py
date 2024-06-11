import pandas as pd


################
# ISO 3166-1 DATA
################

def load_ISO3166_data():
    """
    Load the ISO 3166-1 country codes from the CSV file
    """
    return pd.read_csv("src/data/countries_codes_and_coordinates.csv")


def countryToISO3166_A3(country):
    """
    Get the ISO 3166-1 alpha-3 code for a given country.

    Parameters:
    - country (str): The name of the country, must start with a capital letter.

    Returns:
    - str: The ISO 3166-1 alpha-3 code for the given country.
    """
    ISO3166 = load_ISO3166_data()
    return ISO3166[ISO3166['Country'].astype(str) == country]['Alpha-3 code'].values[0][2:-1]

def ISO3166_A3ToCountry(ISO3166_A3_id):
    """
    Get the name of the country for a given ISO 3166-1 alpha-3 code.

    Parameters:
    - ISO3166_A3 (str): The ISO 3166-1 alpha-3 code for the country.

    Returns:
    - str: The name of the country.
    """
    code = " \""+ ISO3166_A3_id + "\""
    ISO3166 = load_ISO3166_data()
    return ISO3166[ISO3166['Alpha-3 code'].astype(str) == code]['Country'].values[0]