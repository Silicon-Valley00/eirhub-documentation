# Prescription Services

Jump to...
- [Get prescriptions by patient ID](#get-prescription-by-id)
- [Get all prescriptions](#get-all-prescriptions)
- [Create a new prescription by patient ID](#create-a-prescription-for-a-patient)
- [Update prescription by prescription ID](#update-prescription-by-prescription-id)
- [Delete prescription by prescription ID](#delete-prescription-by-prescription-id)

## Get Prescription By patient ID
- GET: /prescription/`idPatient`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/prescription`

- RESPONSE:
    ```json
    {
    "msg": [
        {
        "dosage": "1/x3",
        "drug_name": "Ibuprofen",
        "end_date": "2023-12-31",
        "id": 12,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-19",
        "time_of_administration": "12:23:45"
        },
        {
        "dosage": "1/x2",
        "drug_name": "trimetazol",
        "end_date": "2022-12-31",
        "id": 27,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
        },
        {
        "dosage": "1/x2",
        "drug_name": "paracetamol",
        "end_date": "2022-12-31",
        "id": 28,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
        },
        {
        "dosage": "1/x2",
        "drug_name": "contanitpol",
        "end_date": "2022-12-31",
        "id": 29,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
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
            "dosage": "1/day",
            "drug_name": "lepromax",
            "end_date": "2023-01-31",
            "id": 2,
            "last_taken_date": "2023-01-12",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "2/day",
            "drug_name": "ziprofin ",
            "end_date": "2023-01-31",
            "id": 3,
            "last_taken_date": "2023-01-12",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "1/day",
            "drug_name": "zipodex",
            "end_date": "2023-01-31",
            "id": 4,
            "last_taken_date": "0000-00-00",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "2/day",
            "drug_name": "laravel",
            "end_date": "2022-12-31",
            "id": 6,
            "last_taken_date": "2022-12-31",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "2/day",
            "drug_name": "laravelproxin",
            "end_date": "2022-12-31",
            "id": 7,
            "last_taken_date": "2022-12-31",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
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