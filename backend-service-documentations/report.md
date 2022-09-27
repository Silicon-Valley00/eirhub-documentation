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
            "report_type":"Test results",
            "report_url":"report_url",
            "description":"paternity test results ordered by Dr.Melody Hoppins",
            "id_patient": 30,
            "id_doctor": 22,
            "upload_date": "2022-11-18"
        }
        ```
- SAMPLE URL: `https://base.com/report`
- RESPONSE:
    ```json
     {
    "msg": {
        "description": "paternity test results ordered by Dr.Melody Hoppins",
        "id_doctor": 22,
        "id_patient": 30,
        "id_report": 24,
        "report_type": "Test results",
        "report_url": "report_url",
        "upload_date": "Fri, 18 Nov 2022 00:00:00 GMT"
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
            "report_url": "",
            "upload_date": "Thu, 21 Jul 2022 12:01:21 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "This report is for medication",
            "doctor_first_name": "Gaglo",
            "doctor_last_name": "Nathaniel",
            "id_patient": 30,
            "id_report": 4,
            "report_type": "Medication",
            "report_url": "",
            "upload_date": "Thu, 21 Jul 2022 12:01:51 GMT"
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
            "report_url": "",
            "upload_date": "Sat, 23 Jul 2022 21:36:42 GMT"
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
            "report_url": "",
            "upload_date": "Mon, 08 Aug 2022 17:11:11 GMT"
        },
        "status": true
    },
]
    ```
[Back to the top...](#report-services)



## Delete Report By Report ID
- DELETE: /report/`idReport`
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/report/?id_report=21`
- RESPONSE:
    ```json
     {
    "msg": {
        "description": "This report is for medication",
        "id_report": 18,
        "report_type": "Medication",
        "report_url": "",
        "upload_date": "Thu, 25 Aug 2022 16:00:50 GMT"
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
            "id_report": 3,
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
                "id_report": 3,
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
- SAMPLE URL: `https://base.com/report/30`
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
