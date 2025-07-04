import pandas as pd
import requests
import json
import datetime
API_URL = "http://api.open-notify.org/iss-now.json"
report_file = "iss_location.csv"

def fetch_location():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data=response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error in API: {e}")
        return None

def gen_report():
    data = fetch_location()
    if data:
        times = datetime.datetime.fromtimestamp(data['timestamp'])
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        print(f"Time: {times} having longitude: {lon} and lattitude: {lat}")

        df = pd.DataFrame([{
            "Time":times,
            "Longitude": lon,
            "Latitude": lat
        }])
        df.to_csv(report_file,',',index=False)

lon_list = []
lat_list = []

def gen_lists():
    data = fetch_location()
    if data:
        times = datetime.datetime.fromtimestamp(data['timestamp'])
        lat = data['iss_position']['latitude']
        lon = data['iss_position']['longitude']
        lon_list.append(lon)
        lat_list.append(lat)

for i in range(1,6):
    gen_lists()

print(f"Longitude list: {lon_list} \nLattitude list: {lat_list}")