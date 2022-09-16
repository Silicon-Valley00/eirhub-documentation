# Report Services
Jump to...
- [Create report](#create-report)
- [Get all reports](#get-all-reports)
- [Delete report by report ID](#delete-report-by-report-id)  
- [Update report by report ID](#update-report-by-report-id)
- [Get report by patient ID](#get-report-by-patient-id)

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
            "description": "This report is for medication",
            "idReport": 3,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:21 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "This report is for medication",
            "idReport": 4,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:51 GMT"
        },
        "status": true
    },
    {
        "msg": {
            "description": "This report is for medication",
            "idReport": 5,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:04:12 GMT"
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
- GET: /report/`idReport`
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/report/?id_report=20`
- RESPONSE:
    ```json
        {
        "msg": [
            {
            "description": "This report is for medication",
            "id_report": 3,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:21 GMT"
            },
            {
            "description": "This report is for medication",
            "id_report": 4,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:01:51 GMT"
            },
            {
            "description": "This report is for medication",
            "id_report": 5,
            "report_type": "Medication",
            "upload_date": "Thu, 21 Jul 2022 19:04:12 GMT"
            }
        ],
        "status": true
        }
    ```
[Back to the top...](#report-services)
