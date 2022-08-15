# HealthDetails Services

Jump to...
- [Get health details by patient ID](#get-health-details-by-patient-id)
- [Update Health details](#update-health-details)
- [Create Health Details](#create-health-details)
- [Get all health details](#get-all-health-details)
- [Delete Health Details by ID](#delete-health-details-by-id)



## Get health details by patient ID
- GET: /healthdetails/`patientID`
- BODY PARAMETERS: None
- RESPONSE:
    ```json
    {
        "msg": {
            "blood_group": "B",
            "blood_pressure": 34.6,
            "blood_sugar": "170",
            "bmi": 34.3,
            "height": 99.3,
            "last_visit": "Sun, 08 Sep 2002 00:00:00 GMT",
            "patient_id": 31,
            "pulse": 116.0,
            "respiratory_rate": "25",
            "temperature": 32.5,
            "weight": 87.9
        },
        "status": true
    }   
    ```
[Back to the top...](#healthdetails-services)

## Update Health details
- PUT: /healthdetails/`patientId`
- BODY PARAMETERS:
    - Sample
        ```json
        {
            "last_visit": "2002-09-08",
            "blood_group": "B",
            "blood_pressure": "34.6",
            "respiratory_rate": "116",
            "temperature":"36",
            "pulse": "98.9",
            "blood_sugar": "119",
            "weight": "87.9",
            "height": "132"
        } 	 
        ```
- RESPONSE:
    ```json
        {
    "msg": {
        "blood_group": "B",
        "blood_pressure": 34.6,
        "blood_sugar": "119",
        "bmi": 34.3,
        "height": 132.0,
        "last_visit": "Sun, 08 Sep 2002 00:00:00 GMT",
        "id_patient": 38,
        "pulse": 98.9,
        "respiratory_rate": "116",
        "temperature": 36.0,
        "weight": 87.9
    },
    "status": true
    }   
    ```
[Back to the top...](#healthdetails-services)

## Create Health Details   
- POST: /healthdetails
- BODY PARAMETERS:
    - Sample
        ```json
        {
            "patient_id": "38",
            "last_visit": "2009-09-08",
            "blood_group": "O",
            "bmi": "40.3",
            "blood_pressure": "39.6",
            "respiratory_rate": "Good",
            "temperature": "43.0",
            "pulse": "89.9",
            "blood_sugar": "Plenty",
            "weight": "78.9",
            "height": "99.9"
        }
        ```
- RESPONSE:
    ```json
    {
        "msg": {
            "blood_group": "O",
            "blood_pressure": 39.6,
            "blood_sugar": "Plenty",
            "bmi": 40.3,
            "height": 99.9,
            "last_visit": "Tue, 08 Sep 2009 00:00:00 GMT",
            "patient_id": 38,
            "pulse": 89.9,
            "respiratory_rate": "Good",
            "temperature": 43.0,
            "weight": 78.9
        },
        "status": true
    }
    ```
[Back to the top...](#healthdetails-services)

## Get all health details
- GET: /healthdetails
- BODY PARAMETERS: None
- RESPONSE:
    ```json
    {
    "msg": [
        {
            "blood_group": "A",
            "blood_pressure": 56.0,
            "blood_sugar": "23",
            "bmi": 43.0,
            "height": 1.79,
            "last_visit": "Thu, 12 Jan 2023 00:00:00 GMT",
            "patient_id": 31,
            "pulse": 79.0,
            "respiratory_rate": "75",
            "weight": 25.0
        }
    ],
    "status": true
    }
    ```
[Back to the top...](#healthdetails-services)

## Delete Health Details by ID 
- DELETE: /healthdetails/`idHealthDetails`  
- BODY PARAMETERS: None   
- RESPONSE:
    ```json
    {
    "msg": {
        "blood_group": "A",
        "blood_pressure": 56.0,
        "blood_sugar": "23",
        "bmi": 43.0,
        "height": 1.8,
        "last_visit": "Thu, 12 Jan 2023 00:00:00 GMT",
        "patient_id": 30,
        "pulse": 79.0,
        "respiratory_rate": "75",
        "weight": 25.0
    },
    "status": true
    }
  ```
[Back to the top...](#healthdetails-services)