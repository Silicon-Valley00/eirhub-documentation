# Report Services
Jump to...
- [Errors](#errors)
- [Create report](#create-report)
- [Get all reports](#get-all-reports)
- [Delete report by report ID](#delete-report-by-report-id)  
- [Update report by report ID](#update-report-by-report-id)
- [Get report by patient ID](#get-report-by-patient-id)

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
[Back to the top...](#report-services)

## Create report
- POST: /report
- BODY PARAMETERS:
    - Sample
        ```json
        {
            "report_type":"Lab report",
            "description":"Lab report ordered by Dr.Raymond Brown",
            "uploaddate": "Thu, 21 Jul 2022 19:01:51 GMT"
        }
        ```
- SAMPLE URL: `https://base.com/report`
- RESPONSE:
    ```json
     {
        "msg": {
            "description": "Lab report ordered by Dr.Raymond Brown",
            "idReport": 12,
            "report_type": "Lab report",
	        "uploaddate": "Thu, 21 Jul 2022 19:01:51 GMT"
        },
        "status": true
    }
    ```
[Back to the top...](#report-services)


## Get All reports
- GET: /reports
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/reports`
- RESPONSE:
    ```json
    [
    {
        "msg": {
            "description": "This report is now for urology medication",
            "doctor_first_name": "Kemi",
            "doctor_last_name": "Otedola",
            "id_patient": 30,
            "id_report": 3,
            "report_type": "Urology Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:21 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "This report is for medication",
            "doctor_first_name": "Gaglo",
            "doctor_last_name": "nathaniel",
            "id_patient": 30,
            "id_report": 4,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:51 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "Lab report ordered by Dr.Raymond Brown",
            "doctor_first_name": "Kemi",
            "doctor_last_name": "Otedola",
            "id_patient": 31,
            "id_report": 9,
            "report_type": "Lab report",
            "upload_date": "Sun, 24 Jul 2022 04:36:42 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "covid test conducted by the CDC",
            "doctor_first_name": "Kemi",
            "doctor_last_name": "Otedola",
            "id_patient": 31,
            "id_report": 13,
            "report_type": "Covid-19 test results",
            "upload_date": "Tue, 09 Aug 2022 00:11:11 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "vaccination for chicken Pox",
            "doctor_first_name": "Kemi",
            "doctor_last_name": "Otedola",
            "id_patient": 31,
            "id_report": 16,
            "report_type": "vaccination card",
            "upload_date": "Tue, 09 Aug 2022 00:58:05 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "This report is for medication",
            "doctor_first_name": "Gaglo",
            "doctor_last_name": "nathaniel",
            "id_patient": 34,
            "id_report": 18,
            "report_type": "Medication",
            "upload_date": "Thu, 25 Aug 2022 23:00:50 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "This report is for medication ",
            "doctor_first_name": "Gaglo",
            "doctor_last_name": "nathaniel",
            "id_patient": 31,
            "id_report": 21,
            "report_type": "Medication",
            "upload_date": null
        },
        "status": true
    },
    {
        "msg": {
            "description": "Lab report order by Dr.Gaglo Odartey",
            "doctor_first_name": "Gaglo",
            "doctor_last_name": "nathaniel",
            "id_patient": 34,
            "id_report": 23,
            "report_type": "Lab report",
            "upload_date": "Thu, 21 Jul 2022 19:01:21 GMT"
        },
        "status": true
    }
    ]
    ```
[Back to the top...](#report-services)



## Delete Report By Report ID
- DELETE: /report/`idReport`
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/report/?id_report=20`
- RESPONSE:
    ```json
        {
        "msg": {
            "description": "This report is for medication ",
            "idReport": 3,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:51 GMT"
        },
        "status": true
        }
    ```	
[Back to the top...](#report-services)

## Update Report By Report ID
- PUT: /report/`idReport`
- BODY PARAMETERS:
    - Sample
    ```json
        {
            "description": "This report is for medication ",
            "idReport": 3,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:51 GMT"
        }
    ```
- SAMPLE URL: `https://base.com/report/?id_report=20`
- RESPONSE:
    ```json
        {
            "msg": {
                "description": "This report is for medication ",
                "idReport": 3,
                "report_type": "Medication",
                "uploaddate": "10/08/22"
            },
            "status": true
        }
    ```
[Back to the top...](#report-services)


## Get Report By Patient ID
- GET: /report/`idPatient`
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/report/?id_report=30`
- RESPONSE:
    ```json
        {
    "msg": [
        {
            "description": "This report is now for urology medication",
            "doctor_first_name": "Kemi",
            "doctor_last_name": "Otedola",
            "id_patient": 30,
            "id_report": 3,
            "report_type": "Urology Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:21 GMT"
        },
        {
            "description": "This report is for medication",
            "doctor_first_name": "Gaglo",
            "doctor_last_name": "nathaniel",
            "id_patient": 30,
            "id_report": 4,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:51 GMT"
        }
    ],
    "status": true
        }
    ```
[Back to the top...](#report-services)