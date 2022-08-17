# Appointment Services
Jump to...
- [Errors](#errors)
- [Getting all appointments](#getting-all-appointments-from-table)
- [Getting appointments of a specific patient](#getting-all-appointments-related-to-a-particular-patient-given-the-patients-id)
- [Getting appointments of a specific doctor](#getting-all-appointments-related-to-a-particular-doctor-given-the-doctors-id)
- [Adding appointment to the table](#adding-an-appointment-to-the-table)
- [Updating an appointment](#updating-an-appointment-by-its-id)
- [Deleting an appointment](#deleting-an-appointment-by-providing-its-id)
## Errors
All errors are of the form shown below:
```json
{
    "msg": {
        "dev_message": "Provided patient ID might not exist. +  Error generating reponse message. (actual exception)",
        "message": "Error getting appointments"
    },
    "status": false
}
```
[Back to the top...](#appointment-services)

## Getting all appointments from table
- GET: /appointments
- BODY PARAMETERS: None
- QUERY PARAMETERS: None
- SAMPLE URL: `https://base.com/appointments/`
- Sample response:
    ```json
    {
        "msg": [
            {
                "appointment_date": "Fri, 21 Oct 2022 00:00:00 GMT",
                "appointment_end_time": "11:00:00",
                "appointment_location": "",
                "appointment_reason": "Chest pains",
                "appointment_start_time": "10:00:00",
                "appointment_status": "Declined",
                "doctor_info": {
                    "first_name": "Rexford",
                    "last_name": "Machu",
                    "middle_name": "G.O.A.T.II",
                    "person_image": "..."
                },
                "idAppointment": 3,
                "idDoctor": 21,
                "idPatient": 34,
                "patient_info": {
                    "fist_name": "Pete",
                    "last_name": "Greg",
                    "middle_name": "Leta",
                    "person_image": "..."
                }
            },
            {
                "appointment_date": "Mon, 21 Nov 2022 00:00:00 GMT",
                "appointment_end_time": "03:00:00",
                "appointment_location": "",
                "appointment_reason": "Eczema",
                "appointment_start_time": "01:00:00",
                "appointment_status": "Declined",
                "doctor_info": {
                    "first_name": "Rexford",
                    "last_name": "Machu",
                    "middle_name": "G.O.A.T",
                    "person_image": "..."
                },
                "idAppointment": 5,
                "idDoctor": 20,
                "idPatient": 34,
                "patient_info": {
                    "fist_name": "Pete",
                    "last_name": "Greg",
                    "middle_name": "Leta",
                    "person_image": "..."
                }
            }
        ],
        "status": true
    }
    ```
[Back to the top...](#appointment-services)

## Getting all appointments related to a particular patient given the patient's ID
- GET: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the patient through the query param, `id_patient`. You could also filter more by providing an extra query paramter, `accepted` which could either take values `true` or `false`.
- SAMPLE URL: `https://base.com/appointments/?id_patient=31&accepted=true`
- Sample response:
    ```json
    {
        "msg": [
            {
                "appointment_date": "Fri, 21 Oct 2022 00:00:00 GMT",
                "appointment_end_time": "11:00:00",
                "appointment_location": "",
                "appointment_reason": "Chest pains",
                "appointment_start_time": "10:00:00",
                "appointment_status": "Declined",
                "doctor_info": {
                    "first_name": "Rexford",
                    "last_name": "Machu",
                    "middle_name": "G.O.A.T.II",
                    "person_image": "..."
                },
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
                "doctor_info": {
                    "first_name": "Rexford",
                    "last_name": "Machu",
                    "middle_name": "G.O.A.T",
                    "person_image": "..."
                },
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
                "doctor_info": {
                    "first_name": "Rexford",
                    "last_name": "Machu",
                    "middle_name": "G.O.A.T",
                    "person_image": "..."
                },
                "idAppointment": 5,
                "idDoctor": 20,
                "idPatient": 34
            }
        ],
        "status": true
    }
    ```
[Back to the top...](#appointment-services)

## Getting all appointments related to a particular doctor given the doctor's ID
- GET: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the doctor through the query param, `id_doctor`. You could also filter more by providing an extra query paramter, `accepted` which could either take values `true` or `false`.
- SAMPLE URL: `https://base.com/appointments/?id_doctor=20`
- Sample response:
    ```json
    {
        "msg": [
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
                "patient_info": {
                    "fist_name": "Pete",
                    "last_name": "Greg",
                    "middle_name": "Leta",
                    "person_image": "..."
                }
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
                "patient_info": {
                    "fist_name": "Pete",
                    "last_name": "Greg",
                    "middle_name": "Leta",
                    "person_image": "..."
                }
            }
        ],
        "status": true
    }
    ```
[Back to the top...](#appointment-services)

## Adding an appointment to the table
- POST: /appointments
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
        "msg": [
            {
                "appointment_date": "0000-00-00",
                "appointment_end_time": "09:00:00",
                "appointment_location": "There Naa",
                "appointment_reason": "Death Soon",
                "appointment_start_time": "09:00:00",
                "appointment_status": "Pending",
                "doctor_info": {
                    "first_name": "Rexford",
                    "last_name": "Machu",
                    "middle_name": "G.O.A.T.II",
                    "person_image": "..."
                },
                "idAppointment": 9,
                "idDoctor": 21,
                "idPatient": 31,
                "patient_info": {
                    "fist_name": "Max",
                    "last_name": "Mawube",
                    "middle_name": "Ahiamadzor",
                    "person_image": "..."
                }
            }
        ],
        "status": true
    }
    ```
[Back to the top...](#appointment-services)

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
- QUERY PARAMETERS: Provide the ID of the specific appointment you want to update through query param, `id_appointment`
- SAMPLE URL: `https://base.com/appointments/?id_appointment=9`
- Sample response:

[Back to the top...](#appointment-services)

## Deleting an appointment by providing its ID
- DELETE: /appointments/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the appointment through the query param, `id_appointment`
- SAMPLE URL: `https://base.com/appointments/?id_appointment=10`
- Sample response:
    ```json
    {
        "msg": {
            "appointment_date": "0000-00-00",
            "appointment_end_time": "09:00:00",
            "appointment_location": "There Naa",
            "appointment_reason": "Death Soon",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Pending",
            "doctor_info": {
                "first_name": "Rexford",
                "last_name": "Machu",
                "middle_name": "G.O.A.T.II"
            },
            "idAppointment": 10,
            "idDoctor": 21,
            "idPatient": 31,
            "patient_info": {
                "fist_name": "Max",
                "last_name": "Mawube",
                "middle_name": "Ahiamadzor"
            }
        },
        "status": true
    }
    ```
[Back to the top...](#appointment-services)