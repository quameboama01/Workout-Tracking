import requests

APP_ID = "e9b1b420"
API_KEY = "15eaf1aaa9c1ba07dae66ffecf3cef27"
GENDER = "male"
WEIGHT_KG = 92.50
HEIGHT_CM = 6.25
AGE = 38

headers = {
    "x-api-key": API_KEY,
    "x-app-id": APP_ID,
    #"x-remote-user-id": "0"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text =  input("Tell me what exercise you did today? ")
exercise_config = {
    "query":exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
#response.raise_for_status
results = response.json()
print(results)

sheet_endpoint = "https://api.sheety.co/512493e17f966118373cd869f61856dd/workoutTracking/workouts"
