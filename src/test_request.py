import requests

# The URL and request body for getting admin0 data
url = "https://dtmapi.iom.int/api/IdpAdmin0Data/GetAdmin0Data"
payload = {
    "operation": "Returns and displacement in Afghanistan",
    "countryName": "",
    "admin0Pcode": "AFG",
    "reportingDate": {
        "fromDate": "2017-12-31",
        "toDate": None
    },
    "reportMonthRange": {
        "monthFrom": {
            "year": 2000,
            "month": "1"
        },
        "monthTo": {
            "year": 2024,
            "month": "12"
        }
    },
    "roundNumber": {
        "from": 0,
        "to": 0
    }
}

# Make the request to the API
response = requests.post(url, json=payload)

# Print the response status code and text
print(response.status_code)
print(response.json())