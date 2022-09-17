# Prescription Services

Jump to...
- [Errors](#errors)
- [Get prescriptions by patient ID](#get-prescription-by-patient-id)
- [Get all prescriptions](#get-all-prescriptions)
- [Create a new prescription by patient ID](#create-a-prescription-for-a-patient)
- [Update prescription by prescription ID](#update-prescription-by-prescription-id)
- [Delete prescription by prescription ID](#delete-prescription-by-prescription-id)

## Errors
All errors are of the form shown below:
```json
{
    "msg": {
        "dev_message": "(Actual Exception generated)",
        "message": "Connection Error: Prescriptions not updated"
    },
    "status": false
}
```
[Back to the top...](#prescription-services)

## Get Prescription By patient ID
- GET: /prescription/`idPatient`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/prescription/31`

- RESPONSE:
    ```json
    {
    "msg": [
        {
        "dosage": "1/x3",
        "drug_name": "paracetamol",
        "end_date": "2022-12-31",
        "id": 25,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-10-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "1/x2",
        "drug_name": "trimetazol",
        "end_date": "2022-12-31",
        "id": 26,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "1/x2",
        "drug_name": "Liquzol",
        "end_date": "2022-12-31",
        "id": 37,
        "last_taken_date": "2022-08-14",
        "start_date": "2022-12-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "2/x3",
        "drug_name": "Ibuprofen",
        "end_date": "2022-12-31",
        "id": 38,
        "last_taken_date": "2022-08-27",
        "start_date": "2022-12-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "2/x1",
        "drug_name": "Quinine",
        "end_date": "2022-08-31",
        "id": 42,
        "last_taken_date": "2022-08-01",
        "start_date": "2022-08-01",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "2/x1",
        "drug_name": "monotica",
        "end_date": "2022-12-31",
        "id": 43,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "After Meals"
        }
    ],
    "status": true
    }
    ```
[Back to the top...](#prescription-services)

## Get All Prescriptions
- GET: /prescription 

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/prescription`

- RESPONSE:
    ```json
    {
    "msg": [
        {
        "dosage": "1/x3",
        "drug_name": "paracetamol",
        "end_date": "2022-12-31",
        "id": 25,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-10-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "1/x2",
        "drug_name": "trimetazol",
        "end_date": "2022-12-31",
        "id": 26,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "1/x2",
        "drug_name": "Liquzol",
        "end_date": "2022-12-31",
        "id": 37,
        "last_taken_date": "2022-08-14",
        "start_date": "2022-12-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "2/x3",
        "drug_name": "Ibuprofen",
        "end_date": "2022-12-31",
        "id": 38,
        "last_taken_date": "2022-08-27",
        "start_date": "2022-12-31",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "2/x1",
        "drug_name": "Quinine",
        "end_date": "2022-08-31",
        "id": 42,
        "last_taken_date": "2022-08-01",
        "start_date": "2022-08-01",
        "time_of_administration": "Before Meals"
        },
        {
        "dosage": "2/x1",
        "drug_name": "monotica",
        "end_date": "2022-12-31",
        "id": 43,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "After Meals"
        }
    ],
    "status": true
    }
    ```
[Back to the top...](#prescription-services)

## Create A Prescription For A Patient
- POST : /prescription

- BODY PARAMETERS: 
    - Sample
    ```json
        {
        "drug_name":"laravelS",
        "dosage":"2/day",
        "time_of_administration":"23:59:40",
        "start_date":"2022-12-31",
        "end_date":"2022-12-31",
        "last_taken_date":"2022-12-31",
        "idPatient":28
    }
    ```

- SAMPLE URL: `https://base.com/prescription`

- RESPONSE:
    ```json
   {
    "msg": {
        "dosage": "2/day",
        "drug_name": "laravelS",
        "end_date": "2022-12-31",
        "id": 8,
        "idPatient": 28,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
    },
    "status": true
    ```
[Back to the top...](#prescription-services)

## Update Prescription By Prescription ID
- PUT: /prescription/`idPrescription`
- BODY PARAMETERS:
    - Sample
    ```json
	{
    "drug_name":"laravelS",
    "dosage":"3/day",
    "time_of_administration":"23:59:40",
    "start_date":"2022-12-31",
    "end_date":"2022-12-31",
    "last_taken_date":"2022-12-31",
    "idPatient":28
    }
	```
- SAMPLE URL: `https://base.com/prescription/?id_prescription=20`
- RESPONSE:
    ```json
    {
        "msg": {
            "dosage": "3/day",
            "drug_name": "laravelS",
            "end_date": "2022-12-31",
            "id": 8,
            "idPatient": 28,
            "last_taken_date": "2022-12-31",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        "status": true
    }
    ```
[Back to the top...](#prescription-services)

## Delete Prescription by Prescription ID
- DELETE: /prescription/`idPrescription`
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/prescription/?id_prescription=20`

- RESPONSE:
    ```json
    "msg": {
        "dosage": "2/day",
        "drug_name": "laravel",
        "end_date": "2022-12-31",
        "id": 6,
        "idPatient": 28,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
    },
    "status": true
    ```
[Back to the top...](#prescription-services)