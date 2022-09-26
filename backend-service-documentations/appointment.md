# Appointment Services
Jump to...
- [Errors](#errors)
- [Get all appointments](#get-all-appointments-from-table)
- [Get appointments of a specific patient](#get-all-appointments-related-to-a-particular-patient-given-the-patients-id)
- [Get appointments of a specific doctor](#get-all-appointments-related-to-a-particular-doctor-given-the-doctors-id)
- [Add appointment to the table](#adding-an-appointment-to-the-table)
- [Update an appointment](#update-an-appointment-by-its-id)
- [Get patient's doctors based on patient_id](#get-patients-doctors-based-on-patientid)
- [Get doctor's patients based on doctor_id](#get-doctors-patients-based-on-doctorid)
- [Delete an appointment](#delete-an-appointment-by-providing-its-id)
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

## Get all appointments from table
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

## Get all appointments related to a particular patient given the patient's ID
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

## Get all appointments related to a particular doctor given the doctor's ID
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

## Add an appointment to the table
- POST: /appointments
- BODY PARAMETERS: `application/json`
    - Sample:
        ```json
       {
        "appointment_date": "2022-12-13",
        "appointment_end_time": "09:00:00",
        "appointment_reason": "Boils in nose",
        "appointment_start_time": "09:00:00",
        "appointment_status": "Pending",
        "appointment_location": "Ridge Medical center",
        "id_doctor": 21,
        "id_patient": 30
       } 
        ```
- QUERY PARAMETERS: None
- SAMPLE URL: `https://base.com/appointments/`
- Sample response:
    ```json
   {
    "msg": [
        {
            "appointment_date": "Tue, 13 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_location": "Ridge Medical center",
            "appointment_reason": "Boils in nose",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Pending",
            "doctor_info": {
                "first_name": "Rexford",
                "last_name": "Machu",
                "middle_name": "G.O.A.T.II",
                "person_image": "https://img.com/G.O.A.T.II"
            },
            "id_appointment": 29,
            "id_doctor": 21,
            "id_patient": 30,
            "patient_info": {
                "first_name": "Molly",
                "last_name": "Malloy",
                "middle_name": "Patient",
                "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI"
            }
        }
    ],
    "status": true
   }
    ```
[Back to the top...](#appointment-services)

## Update an appointment by its ID
- PUT: /appointments/
- BODY PARAMETERS: `application/json`
    - Sample:
        ```json
        {
            "appointment_date": "2022-12-12",
            "appointment_end_time": "12:00:00",
            "appointment_reason": "Severe abdominal pains",
            "appointment_status" : "Declined",
            "appointment_start_time": "09:00:00",       
            "appointment_location": "North Legon Hospital",
            "id_doctor": 23,
            "id_patient": 34
        }
        ```
- QUERY PARAMETERS: Provide the ID of the specific appointment you want to update through query param, `id_appointment`
- SAMPLE URL: `https://base.com/appointments/?id_appointment=9`
- Sample response:
    ```json
    {
    "msg": [
        {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "12:00:00",
            "appointment_location": "North Legon Hospital",
            "appointment_reason": "Severe abdominal pains",
            "appointment_start_time": "09:00:00",
            "appointment_status": "Declined",
            "doctor_info": {
                "first_name": "Janice",
                "last_name": "Brempong",
                "middle_name": "Oluwa",
                "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg"
            },
            "id_appointment": 6,
            "id_doctor": 23,
            "id_patient": 34,
            "patient_info": {
                "fist_name": "Pete",
                "last_name": "Greg",
                "middle_name": "Leta",
                "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI"
            }
        }
    ],
    "status": true
    }
    ```

[Back to the top...](#appointment-services)

## Get patient's doctors based on patient_id
- GET: /appointmentspatients/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the patient through the query param, `id_patient`
- SAMPLE URL: `https://base.com/appointmentspatients/?id_patient=34`
- Sample response:
    ```json
   {
    "msg": [
       
        {
            "date_of_birth": "Wed, 21 Sep 1994 00:00:00 GMT",
            "doctor_ratings": 4,
            "doctor_specialties": "Obstetrics",
            "first_name": "Janice",
            "gender": "Female",
            "hospital_code": "NL05",
            "hospital_name": "North Legon Hospital",
            "house_address": "House-64",
            "id_doctor": 23,
            "id_message": "",
            "last_name": "Brempong",
            "license_number": "80043248",
            "middle_name": "Ama",
            "person_image": "http://res.cloudinary.com/eirhub-siliconvalley/image/upload/v1662052543/doctor_images/lkfnkpvitofadlqgxcna.jpg",
            "user_email": "janice@gmail.com"
        },
        {
            "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
            "doctor_ratings": 3,
            "doctor_specialties": "Gynaecology, Paediatric, General",
            "first_name": "Rexford",
            "gender": "Male",
            "hospital_code": "0",
            "hospital_name": "",
            "house_address": "House-4",
            "id_doctor": 21,
            "id_message": "",
            "last_name": "Machu",
            "license_number": "8003490390",
            "middle_name": "G.O.A.T.II",
            "person_image": "https://img.com/G.O.A.T.II",
            "user_email": "baddest70@st.knust.edu.gh"
        }
    ],
    "status": true
    }
    ```
[Back to the top...](#appointment-services)

## Get doctor's patients based on doctor_id
- GET: /appointmentsdoctors/
- BODY PARAMETERS: None
- QUERY PARAMETERS: Provide the ID of the doctor through the query param, `id_doctor`
- SAMPLE URL: `https://base.com/appointmentsdoctors/?id_doctor=22`
- Sample response:
    ```json
   {
    "msg": [
        {
            "date_of_birth": "Tue, 03 Jul 2001 00:00:00 GMT",
            "first_name": "Pete",
            "gender": "male",
            "house_address": "12 sesame street",
            "id_doctor": 22,
            "id_guardian": 20,
            "id_message": "",
            "id_number": "GHA-08006335HJJ",
            "id_patient": 34,
            "last_name": "Greg",
            "middle_name": "Leta",
            "nationality": "Ghanaian",
            "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
            "phone_number": "+233265936575",
            "user_email": "Gregy@st.knust.edu.gh"
        }
       
    ],
    "status": true
      }
    ```
[Back to the top...](#appointment-services)

## Delete an appointment by providing its ID
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