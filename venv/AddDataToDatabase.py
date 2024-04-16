import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("venv/ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerec-e27d4-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "4723":
        {
            "id": 4723,
            "name": "Swapnali Patil",
            "major": "Cyber Security",
            "starting_year": 2020,
            "total_attendance": 8,
            "year": 3,
            "last_attendance_time": "2023-11-20 00:16:28"
        },
    "4724":
        {
            "id": 4724,
            "name": "Prajakta Thorat",
            "major": "Big Data",
            "starting_year": 2021,
            "total_attendance": 12,
            "year": 2,
            "last_attendance_time": "2023-11-15 00:12:34"
        },
    "4725":
        {
            "id": 4725,
            "name": "Priya Rajak",
            "major": "Ubiqutous Computing",
            "starting_year": 2022,
            "total_attendance": 7,
            "year": 1,
            "last_attendance_time": "2023-11-12 00:12:34"
        },
    "4726":
        {
            "id": 4726,
            "name": "Omkar Patil",
            "major": "Blockchain",
            "starting_year": 2022,
            "total_attendance": 10,
            "year": 1,
            "last_attendance_time": "2023-11-16 00:12:34"
        },
    "4727":
        {
             "id": 4727,
            "name": "Mansi Rajak",
            "major": "Artificial Intelligence",
            "starting_year": 2021,
            "total_attendance": 15,
          
            "year": 3,
            "last_attendance_time": "2023-11-16 00:12:34"
        }
}
for key, value in data.items():
    ref.child(key).set(value)