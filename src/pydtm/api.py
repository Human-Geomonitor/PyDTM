# Code by David Gerard (https://github.com/David-GERARD) for the Human GeoMonitor project (https://github.com/Human-Geomonitor)
# This Python API wrapper connects to the IOM's DTM API (https://dtm.iom.int/data-and-analysis/dtm-api) to get data on Internally Displaced Persons (IDPs) in different countries.

import requests
import pandas as pd

def countryLevelData(operation:str = "", countryName:str = "", admin0Pcode:str = "", fromDate:str = None, toDate:str = None, monthFrom_month:str = None,monthFrom_year:int = None, monthTo_month:str = None,monthTo_year:str = None, roundFrom:int = None, roundTo:int = None, to_pandas:bool = False):
    """Get country level data from IOM's DTM API.
    
    :param operation: The operation to perform, default to ""
    :type operation: str
    :param countryName: The name of the country, default to "", must not be specified if using admin0Pcode
    :type countryName: str
    :param admin0Pcode: The admin0Pcode of the country (ISO 3166-1 alpha-3), default to "", must not be specified if using countryName
    :type admin0Pcode: str
    :param fromDate: The start date of the reporting period (format: "yyyy-mm-dd"), optional
    :type fromDate: str
    :param toDate: The end date of the reporting period (format: "yyyy-mm-dd"), optional
    :type toDate: str
    :param monthFrom_month: The start month of the reporting period, default to None
    :type monthFrom_month: str
    :param monthFrom_year: The start year of the reporting period, default to None
    :type monthFrom_year: int
    :param monthTo_month: The end month of the reporting period, default to None
    :type monthTo_month: str
    :param monthTo_year: The end year of the reporting period, default to None
    :type monthTo_year: int
    :param roundFrom: The start round number, default to None, optional
    :type roundFrom: int
    :param roundTo: The end round number, default to None, optional
    :type roundTo: int
    :param to_pandas: Convert the response to a pandas DataFrame, default to False, optional
    :type to_pandas: bool

    :return: The response from the API
    :rtype: dict or pandas.DataFrame depending on the value of to_pandas

    """
    # Check if all required parameters are provided
    if countryName == "" and admin0Pcode == "":
        raise  ValueError("Please provide either the countryName or the admin0Pcode")
    
    if countryName != "" and admin0Pcode != "":
        raise  ValueError("Please provide either the countryName or the admin0Pcode, not both")
    
    if monthFrom_month == None:
        raise ValueError("Please provide the start month of the reporting period (str)") 
    
    if monthFrom_year == None:
        raise ValueError("Please provide the start year of the reporting period (int)")
    
    if monthTo_month == None:
        raise ValueError("Please provide the end month of the reporting period (str)")
    
    if monthTo_year == None:
        raise ValueError("Please provide the end year of the reporting period (int)")

    # The URL for getting admin0 data
    url = "https://dtmapi.iom.int/api/IdpAdmin0Data/GetAdmin0Data"

    # The request body
    payload = {
        "operation": operation,
        "countryName": countryName,
        "admin0Pcode": admin0Pcode,
        "reportingDate": {
            "fromDate": fromDate,
            "toDate": toDate
        },
        "reportMonthRange": {
            "monthFrom": {
                "year": monthFrom_year,
                "month": monthFrom_month
            },
            "monthTo": {
                "year": monthTo_year,
                "month": monthTo_month
            }
        },
        "roundNumber": {
            "from": roundFrom,
            "to": roundTo
        }
    }

    response = requests.post(url, json=payload).json()
    if to_pandas:
        if response['statusCode'] == 200:
            return(pd.DataFrame(response['result']))
        elif response['statusCode'] == 204:
            raise ValueError("No data found in the DTM API for the given parameters")
        else:
            raise ValueError(response['errorMessages'])
    else:
        return(response)



def admin1LevelData(operation:str = "", countryName:str = "", admin0Pcode:str = "", fromDate:str = None, toDate:str = None, monthFrom_month:str = None,monthFrom_year:int = None, monthTo_month:str = None,monthTo_year:str = None, roundFrom:int = None, roundTo:int = None,to_pandas:bool = False):
    """Get admin1 level data from IOM's DTM API.
    
    :param operation: The operation to perform, default to ""
    :type operation: str
    :param countryName: The name of the country, default to "", must not be specified if using admin0Pcode
    :type countryName: str
    :param admin0Pcode: The admin0Pcode of the country (ISO 3166-1 alpha-3), default to "", must not be specified if using countryName
    :type admin0Pcode: str
    :param fromDate: The start date of the reporting period (format: "yyyy-mm-dd"), optional
    :type fromDate: str
    :param toDate: The end date of the reporting period (format: "yyyy-mm-dd"), optional
    :type toDate: str
    :param monthFrom_month: The start month of the reporting period, default to None
    :type monthFrom_month: str
    :param monthFrom_year: The start year of the reporting period, default to None
    :type monthFrom_year: int
    :param monthTo_month: The end month of the reporting period, default to None
    :type monthTo_month: str
    :param monthTo_year: The end year of the reporting period, default to None
    :type monthTo_year: int
    :param roundFrom: The start round number, default to None, optional
    :type roundFrom: int
    :param roundTo: The end round number, default to None, optional
    :type roundTo: int
    :param to_pandas: Convert the response to a pandas DataFrame, default to False, optional
    :type to_pandas: bool

    :return: The response from the API
    :rtype: dict or pandas.DataFrame depending on the value of to_pandas

    """
    # Check if all required parameters are provided
    if countryName == "" and admin0Pcode == "":
        raise  ValueError("Please provide either the countryName or the admin0Pcode")
    
    if countryName != "" and admin0Pcode != "":
        raise  ValueError("Please provide either the countryName or the admin0Pcode, not both")
    
    if monthFrom_month == None:
        raise ValueError("Please provide the start month of the reporting period (str)") 
    
    if monthFrom_year == None:
        raise ValueError("Please provide the start year of the reporting period (int)")
    
    if monthTo_month == None:
        raise ValueError("Please provide the end month of the reporting period (str)")
    
    if monthTo_year == None:
        raise ValueError("Please provide the end year of the reporting period (int)")

    # The URL for getting admin0 data
    url = "https://dtmapi.iom.int/api/IdpAdmin1Data/GetAdmin1Data"

    # The request body
    payload = {
        "operation": operation,
        "countryName": countryName,
        "admin0Pcode": admin0Pcode,
        "reportingDate": {
            "fromDate": fromDate,
            "toDate": toDate
        },
        "reportMonthRange": {
            "monthFrom": {
                "year": monthFrom_year,
                "month": monthFrom_month
            },
            "monthTo": {
                "year": monthTo_year,
                "month": monthTo_month
            }
        },
        "roundNumber": {
            "from": roundFrom,
            "to": roundTo
        },
    }
    response = requests.post(url, json=payload).json()
    if to_pandas:
        if response['statusCode'] == 200:
            return(pd.DataFrame(response['result']))
        elif response['statusCode'] == 204:
            raise ValueError("No data found in the DTM API for the given parameters")
        else:
            raise ValueError(response['errorMessages'])
    else:
        return(response)



def admin2LevelData(operation:str = "", countryName:str = "", admin0Pcode:str = "", fromDate:str = None, toDate:str = None, monthFrom_month:str = None,monthFrom_year:int = None, monthTo_month:str = None,monthTo_year:str = None, roundFrom:int = None, roundTo:int = None, to_pandas:bool = False):
    """Get admin2 level data from IOM's DTM API.
    
    :param operation: The operation to perform, default to ""
    :type operation: str
    :param countryName: The name of the country, default to "", must not be specified if using admin0Pcode
    :type countryName: str
    :param admin0Pcode: The admin0Pcode of the country (ISO 3166-1 alpha-3), default to "", must not be specified if using countryName
    :type admin0Pcode: str
    :param fromDate: The start date of the reporting period (format: "yyyy-mm-dd"), optional
    :type fromDate: str
    :param toDate: The end date of the reporting period (format: "yyyy-mm-dd"), optional
    :type toDate: str
    :param monthFrom_month: The start month of the reporting period, default to None
    :type monthFrom_month: str
    :param monthFrom_year: The start year of the reporting period, default to None
    :type monthFrom_year: int
    :param monthTo_month: The end month of the reporting period, default to None
    :type monthTo_month: str
    :param monthTo_year: The end year of the reporting period, default to None
    :type monthTo_year: int
    :param roundFrom: The start round number, default to None, optional
    :type roundFrom: int
    :param roundTo: The end round number, default to None, optional
    :type roundTo: int
    :param to_pandas: Convert the response to a pandas DataFrame, default to False, optional
    :type to_pandas: bool

    :return: The response from the API
    :rtype: dict or pandas.DataFrame depending on the value of to_pandas

    """
    # Check if all required parameters are provided
    if countryName == "" and admin0Pcode == "":
        raise  ValueError("Please provide either the countryName or the admin0Pcode")
    
    if countryName != "" and admin0Pcode != "":
        raise  ValueError("Please provide either the countryName or the admin0Pcode, not both")
    
    if monthFrom_month == None:
        raise ValueError("Please provide the start month of the reporting period (str)") 
    
    if monthFrom_year == None:
        raise ValueError("Please provide the start year of the reporting period (int)")
    
    if monthTo_month == None:
        raise ValueError("Please provide the end month of the reporting period (str)")
    
    if monthTo_year == None:
        raise ValueError("Please provide the end year of the reporting period (int)")

    # The URL for getting admin0 data
    url = "https://dtmapi.iom.int/api/IdpAdmin2Data/GetAdmin2Data"

    # The request body
    payload = {
        "operation": operation,
        "countryName": countryName,
        "admin0Pcode": admin0Pcode,
        "reportingDate": {
            "fromDate": fromDate,
            "toDate": toDate
        },
        "reportMonthRange": {
            "monthFrom": {
                "year": monthFrom_year,
                "month": monthFrom_month
            },
            "monthTo": {
                "year": monthTo_year,
                "month": monthTo_month
            }
        },
        "roundNumber": {
            "from": roundFrom,
            "to": roundTo
        },
    }
    response = requests.post(url, json=payload).json()
    if to_pandas:
        if response['statusCode'] == 200:
            return(pd.DataFrame(response['result']))
        elif response['statusCode'] == 204:
            raise ValueError("No data found in the DTM API for the given parameters")
        else:
            raise ValueError(response['errorMessages'])
    else:
        return(response)