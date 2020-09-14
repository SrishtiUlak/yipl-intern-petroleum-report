import json
import requests


def fechPetroleumData():
    """Get Data from json file"""
    apiUrl= 'https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json'
    response = requests.get(apiUrl)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
     return None

