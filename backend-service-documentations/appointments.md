# Appointment Services
## Errors
All erros are of the form shown below:
```json
{
    "detail": {
        "description": "Error generating reponse message.",
        "dev_message": "Provided patient ID might not exist.",
        "message": "Error getting appointments"
    },
    "status": false
}
```

## Getting all appointments from table
- GET: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: None
- SAMPLE URL: `https://base.com/appointments/`
- Sample response:
    ```json
    {
        "detail": [
            {
                "appointment_date": "Fri, 21 Oct 2022 00:00:00 GMT",
                "appointment_end_time": "11:00:00",
                "appointment_location": "",
                "appointment_reason": "Chest pains",
                "appointment_start_time": "10:00:00",
                "appointment_status": "Declined",
                "doctor_names": [
                    "Rexford",
                    "G.O.A.T.II",
                    "Machu"
                ],
                "idAppointment": 3,
                "idDoctor": 21,
                "idPatient": 34,
                "patient_names": [
                    "Pete",
                    "Leta",
                    "Greg"
                ]
            },
            {
                "appointment_date": "Mon, 21 Nov 2022 00:00:00 GMT",
                "appointment_end_time": "03:00:00",
                "appointment_location": "",
                "appointment_reason": "Eczema",
                "appointment_start_time": "01:00:00",
                "appointment_status": "Declined",
                "doctor_names": [
                    "Rexford",
                    "G.O.A.T",
                    "Machu"
                ],
                "idAppointment": 5,
                "idDoctor": 20,
                "idPatient": 34,
                "patient_names": [
                    "Pete",
                    "Leta",
                    "Greg"
                ]
            }
        ],
        "status": true
    }
    ```

## Getting all appointments related to a particular patient given the patient's ID
- GET: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the patient through the query param, `patient_id`. You could also filter more by providing an extra query paramter, `accepted` which could either take values `true` or `false`.
- SAMPLE URL: `https://base.com/appointments/?patient_id=31`
- Sample response:
    ```json
    {
        "detail": [
            {
                "appointment_date": "Fri, 21 Oct 2022 00:00:00 GMT",
                "appointment_end_time": "11:00:00",
                "appointment_location": "",
                "appointment_reason": "Chest pains",
                "appointment_start_time": "10:00:00",
                "appointment_status": "Declined",
                "doctor_names": [
                    "Rexford",
                    "G.O.A.T.II",
                    "Machu"
                ],
                "idAppointment": 3,
                "idDoctor": 21,
                "idPatient": 34
            },
            {
                "appointment_date": "Mon, 21 Nov 2022 00:00:00 GMT",
                "appointment_end_time": "13:00:00",
                "appointment_location": "",
                "appointment_reason": "Swollen tonsils",
                "appointment_start_time": "12:00:00",
                "appointment_status": "Accepted",
                "doctor_names": [
                    "Rexford",
                    "G.O.A.T",
                    "Machu"
                ],
                "idAppointment": 4,
                "idDoctor": 20,
                "idPatient": 34
            },
            {
                "appointment_date": "Mon, 21 Nov 2022 00:00:00 GMT",
                "appointment_end_time": "03:00:00",
                "appointment_location": "",
                "appointment_reason": "Eczema",
                "appointment_start_time": "01:00:00",
                "appointment_status": "Declined",
                "doctor_names": [
                    "Rexford",
                    "G.O.A.T",
                    "Machu"
                ],
                "idAppointment": 5,
                "idDoctor": 20,
                "idPatient": 34
            }
        ],
        "status": true
    }
    ```

## Getting all appointments related to a particular doctor given the doctor's ID
- GET: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the doctor through the query param, `doctor_id`. You could also filter more by providing an extra query paramter, `accepted` which could either take values `true` or `false`.
- SAMPLE URL: `https://base.com/appointments/?doctor_id=20`
- Sample response:
    ```json
    {
        "detail": [
            {
                "appointment_date": "Mon, 21 Nov 2022 00:00:00 GMT",
                "appointment_end_time": "13:00:00",
                "appointment_location": "",
                "appointment_reason": "Swollen tonsils",
                "appointment_start_time": "12:00:00",
                "appointment_status": "Accepted",
                "idAppointment": 4,
                "idDoctor": 20,
                "idPatient": 34,
                "patient_names": [
                    "Pete",
                    "Leta",
                    "Greg"
                ]
            },
            {
                "appointment_date": "Mon, 21 Nov 2022 00:00:00 GMT",
                "appointment_end_time": "03:00:00",
                "appointment_location": "",
                "appointment_reason": "Eczema",
                "appointment_start_time": "01:00:00",
                "appointment_status": "Declined",
                "idAppointment": 5,
                "idDoctor": 20,
                "idPatient": 34,
                "patient_names": [
                    "Pete",
                    "Leta",
                    "Greg"
                ]
            }
        ],
        "status": true
    }
    ```

## Adding an appointment to the table
- POST: /appointments/
- BODY PARAMETERS: `application/json`
    - Sample:
        ```json
        {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_reason": "Death Soon",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Pending",
            "appointment_location": "There Naa",
            "idDoctor": 21,
            "idPatient": 31
        }
        ```
- QUERY PARAMETERS: None
- SAMPLE URL: `https://base.com/appointments/`
- Sample response:
    ```json
    {
        "detail": {
            "appointment_date": "0000-00-00",
            "appointment_end_time": "09:00:00",
            "appointment_location": "There Naa",
            "appointment_reason": "Death Soon",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Pending",
            "doctor_names": [
                "Rexford",
                "G.O.A.T.II",
                "Machu"
            ],
            "idAppointment": 9,
            "idDoctor": 21,
            "idPatient": 31,
            "patient_names": [
                "Max",
                "Ahiamadzor",
                "Mawube"
            ]
        },
        "status": true
    }
    ```

## Updating an appointment by its ID
- PUT: /appointments/
- BODY PARAMETERS: `application/json`
    - Sample:
        ```json
        {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_reason": "Death Soon",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Accepted",
            "appointment_location": "There Naa",
            "idDoctor": 21,
            "idPatient": 31
        }
        ```
- QUERY PARAMETERS: Provide the ID of the specific appointment you want to update through query param, `appointment_id`
- SAMPLE URL: `https://base.com/appointments/?appointment_id=9`
- Sample response:

## Deleting an appointment by providing its ID
- DELETE: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the appointment through the query param, `appointment_id`
- SAMPLE URL: `https://base.com/appointments/?appointment_id=9`
- Sample response:
    ```json
    {
        "detail": {
            "appointment_date": "0000-00-00",
            "appointment_end_time": "09:00:00",
            "appointment_location": "There Naa",
            "appointment_reason": "Death Soon",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Pending",
            "doctor_names": "",
            "idAppointment": 10,
            "idDoctor": 21,
            "idPatient": 31,
            "patient_names": ""
        },
        "status": true
    }
    ```