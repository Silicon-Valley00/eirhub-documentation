# HealthDetails Services

Jump to...
- [Errors](#errors)
- [Get health details by patient ID](#get-health-details-by-patient-id)
- [Update Health details](#update-health-details)
- [Create Health Details](#create-health-details)
- [Get all health details](#get-all-health-details)
- [Delete Health Details by ID](#delete-health-details-by-id)

## Errors
All errors are of the form shown below:
```json
{
    "msg": {
        "dev_message": "(Actual Exception generated)",
        "message": "Could not update health details"
    },
    "status": false
}
```
[Back to the top...](#doctor-services)


## Get health details by patient ID
- GET: /healthdetails/`patientID`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/healthdetails/34` 

- RESPONSE:
    ```json
    {
    "msg": {
        "blood_group": "AB",
        "blood_pressure": "120/80",
        "blood_sugar": "170",
        "bmi": 34.3,
        "height": 148.0,
        "id_patient": 38,
        "last_visit": "Mon, 08 Aug 2022 00:00:00 GMT",
        "pulse": 116.0,
        "respiratory_rate": "116",
        "temperature": 34.6,
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
            "last_visit": "2022-08-08",
            "blood_group": "AB",
            "blood_pressure": "120/80",
            "respiratory_rate": "116",
            "temperature":"34.6",
            "pulse": "116",
            "blood_sugar": "170",
            "weight": "87.9",
            "height": "148"
        } 	 
        ```
- SAMPLE URL: `https://base.com/healthdetails/34` 

- RESPONSE:
    ```json
    {
    "msg": {
        "blood_group": "AB",
        "blood_pressure": "120/80",
        "blood_sugar": "170",
        "height": 148.0,
        "id_patient": 38,
        "last_visit": "Mon, 08 Aug 2022 00:00:00 GMT",
        "pulse": 116.0,
        "respiratory_rate": "116",
        "temperature": 34.6,
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

- SAMPLE URL: `https://base.com/healthdetails` 

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

- SAMPLE URL: `https://base.com/healthdetails` 

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

- SAMPLE URL: `https://base.com/healthdetails/6` 

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