#!/usr/bin/env python3
import requests
import pandas as pd
import sys

# This script does not work as is. I tried to get this script to work with a number of Apache NiFi processors,
# such as ExecuteScript, ExecuteStreamCommand, and ExecuteProcess, but I couldn't get it to run,

df = pd.read_csv(sys.stdin)
geoid_list = []
for i in range(len(df)):
    street = df['street'][i]
    city = df['city'][i]
    state = df['state'][i]
    response = requests.get("https://geocoding.geo.census.gov/geocoder/geographies/"
                            f"address?street={street}&city={city}&state={state}&"
                            "benchmark=Public_AR_Census2010&vintage=Census2010_Census2010&layers=10&format=json")
    if response.status_code == 200:
        data = response.json()
        identifier = data['result']['addressMatches'][0]['geographies']['Census Tracts'][0]['GEOID']
        geoid = '14000US' + identifier
        geoid_list.append(geoid)
    else:
        print('Error: ' + str(response.status_code))
dataset = pd.DataFrame({'geo_id': geoid_list})
dataset.to_csv(sys.stdout, index=False)
