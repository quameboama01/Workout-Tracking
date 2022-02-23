import requests
import datetime as dt
from requests.auth import HTTPBasicAuth

APP_ID = 'e9b1b420'
API_KEY = 'f1deb0e16fe58a767548f4442e3a080e'

GENDER = 'male'
WEIGHT_KG = 92.5
HEIGHT_CM = 168
AGE = 38

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me what exercise you did today? ")

exercise_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=exercise_endpoint,
                         headers=headers, json=exercise_config)
results = response.json()


# ******************************* New Configuration *************************************
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/512493e17f966118373cd869f61856dd/workoutTracking/workouts"

for exercise in results["exercises"]:
    sheety_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    res = requests.post(url=sheety_endpoint,
                        json=sheety_config, auth=("andrews", "prayer01"))
    res.raise_for_status()
    print(res.text)
