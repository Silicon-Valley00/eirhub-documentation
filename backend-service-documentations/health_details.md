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
        "message": "Connection Error: Patient health details not updated"
    },
    "status": false
}
```
[Back to the top...](#healthdetails-services)


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
            "id_patient": "42",
            "last_visit": "2021-09-08",
            "blood_group": "A",
            "blood_pressure": "150/80",
            "respiratory_rate": "20",
            "temperature": "37.0",
            "pulse": "116",
            "blood_sugar": "120",
            "weight": "52",
            "height": "173"
        }
        ```

- SAMPLE URL: `https://base.com/healthdetails` 

- RESPONSE:
    ```json
    {
    "msg": {
        "blood_group": "A",
        "blood_pressure": "150/80",
        "blood_sugar": "120",
        "height": 173.0,
        "id_patient": 42,
        "last_visit": "Wed, 08 Sep 2021 00:00:00 GMT",
        "pulse": 116.0,
        "respiratory_rate": "20",
        "temperature": 37.0,
        "weight": 52.0
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
            "blood_pressure": "10/120",
            "blood_sugar": "20",
            "height": 200.0,
            "id_patient": 31,
            "last_visit": "Mon, 10 Aug 2009 00:00:00 GMT",
            "pulse": 29.0,
            "respiratory_rate": "34",
            "temperature": 36.3,
            "weight": 90.0
        },
        {
            "blood_group": "O",
            "blood_pressure": "120/120",
            "blood_sugar": "119",
            "height": 132.0,
            "id_patient": 30,
            "last_visit": "Thu, 08 Sep 2022 00:00:00 GMT",
            "pulse": 116.0,
            "respiratory_rate": "119",
            "temperature": 34.0,
            "weight": 87.9
        }
    ]
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
        "height": 1.8,
        "last_visit": "Thu, 12 Jan 2023 00:00:00 GMT",
        "id_patient": 30,
        "pulse": 79.0,
        "respiratory_rate": "75",
        "weight": 25.0
    },
    "status": true
    }
  ```
[Back to the top...](#healthdetails-services)