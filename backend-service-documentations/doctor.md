# Doctor Services

Jump to...
- [Errors](#errors)
- [Doctor Signup](#doctor-signup)
- [Doctor login](#doctor-login)
- [Get all doctors](#get-all-doctors)
- [Update Doctor by ID](#update-doctor-by-id)
- [Get Doctor by ID](#get-doctor-by-id)
- [Get Number of Patients assigned to Doctor](#get-number-of-patients-assigned-to-doctor)
- [Get Number of Reports assigned to Doctor](#get-number-of-reports-assigned-to-doctor)
- [Get Number of Appointments assigned to Doctor](#get-number-of-appointments-assigned-to-doctor)

## Errors
All errors are of the form shown below:
```json
{
    "msg": {
        "dev_message": "(Actual Exception generated)",
        "message": "Could not update doctor details"
    },
    "status": false
}
```
[Back to the top...](#doctor-services)

## Doctor Signup		
- POST : /doctor/signup      
- BODY PARAMETERS: 
    - Sample:
        ```json
       {
            "first_name": "Benedict",
            "last_name": "Freeman",
            "user_email":"Freeman@gmail.com",
            "user_password":"freeben1990",
            "date_of_birth":"1990-12-18",
            "hospital_code":"RMC04"
        }
        ```
- SAMPLE URL: `https://base.com/doctor/signup`          
- RESPONSE:
	```json
       {
    "msg": {
        "date_of_birth": "Tue, 18 Dec 1990 00:00:00 GMT",
        "first_name": "Benedict",
        "gender": null,
        "hospital_code": "RMC04",
        "hospital_name": "Ridge Medical Center",
        "id_doctor": 28,
        "last_name": "Freeman",
        "license_number": null,
        "middle_name": null,
        "user_email": "Freeman@gmail.com"
    },
    "status": true
    }
	```    
[Back to the top...](#doctor-services)

## Doctor Login			
- POST : /doctor/login
- BODY PARAMETERS:`application/json`
    - Sample:
        ```json
        {
        "user_email":"nathaniel@gmail.com",
        "user_password":"Elormpassword"
        }
        ```
- SAMPLE URL: `https://base.com/doctor/login`        
- RESPONSE:
    ```json
       {
    "msg": {
        "date_of_birth": "Tue, 04 Oct 1988 00:00:00 GMT",
        "first_name": "Gaglo",
        "gender": "Male",
        "id_doctor": 22,
        "last_name": "Nathaniel",
        "license_number": "80043267",
        "middle_name": "Elorm",
        "user_email": "nathaniel@gmail.com"
    },
    "status": true
      }
	```



[Back to the top...](#doctor-services)

## Get All Doctors		
- GET : /doctors      
- BODY PARAMETERS: None
- SAMPLE URL: `https://base.com/doctors`  
- RESPONSE:
	```json
       {
    "msg": [
       {
            "date_of_birth": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "doctor_ratings": 3,
            "doctor_specialties": "Oncology",
            "first_name": "Gaglo",
            "gender": "Male",
            "hospital_code": "KAT02",
            "hospital_name": "Komfo Anokye Teaching Hospital",
            "house_address": "House-5",
            "id_doctor": 22,
            "last_name": "Nathaniel",
            "license_number": "80043267",
            "middle_name": "Elorm",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "nathaniel@gmail.com"
        },
        {
            "date_of_birth": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
            "doctor_ratings": 4,
            "doctor_specialties": "Obstetrics",
            "first_name": "Janice",
            "gender": "Female",
            "hospital_code": "NL05",
            "hospital_name": "North Legon Hospital",
            "house_address": "House-64",
            "id_doctor": 23,
            "last_name": "Brempong",
            "license_number": "80043248",
            "middle_name": "Abena",
            "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
            "user_email": "janice@gmail.com"
        },
    ]
    }
	```    

[Back to the top...](#doctor-services)

## Update Doctor By Id
- PUT : /doctor/`doctorId`
- BODY PARAMETERS: `application/json`	
    - Sample:
        ```json
       {

            "first_name": "Gaglo",
            "middle_name": "Elorm",
            "last_name": "Nathaniel",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "nathaniel@gmail.com",
            "date_of_birth": "1988-10-04",
            "house_address": "House-5",
            "license_number": "80043267",
            "doctor_specialties": "Oncology",
            "gender": "Male",
            "hospital_code": "KAT02"
        
        }

	    ```
- SAMPLE URL: `https://base.com/doctor/21`  
- RESPONSE:
    ```json
     {
    "msg": {
        "date_of_birth": "Tue, 04 Oct 1988 00:00:00 GMT",
        "doctor_ratings": 3,
        "doctor_specialties": "Oncology",
        "first_name": "Gaglo",
        "gender": "Male",
        "hospital_code": "KAT02",
        "hospital_name": "Komfo Anokye Teaching Hospital",
        "house_address": "House-5",
        "id_doctor": 22,
        "last_name": "Nathaniel",
        "license_number": "80043267",
        "middle_name": "Elorm",
        "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
        "user_email": "nathaniel@gmail.com"
    },
    "status": true
    }
        ```    

    
[Back to the top...](#doctor-services)

## Get Doctor By Id		
- GET : /doctor/`doctorId`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/doctor/21` 

- RESPONSE:
	```json
     {
    "msg": {
        "date_of_birth": "Mon, 19 Sep 1994 00:00:00 GMT",
        "doctor_ratings": 4,
        "doctor_specialties": "Obstetrics",
        "first_name": "Janice",
        "gender": "Female",
        "hospital_code": "NL05",
        "hospital_name": "North Legon Hospital",
        "house_address": "House-64",
        "id_doctor": 23,
        "last_name": "Brempong",
        "license_number": "80043248",
        "middle_name": "Abena",
        "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
        "user_email": "janice@gmail.com"
    },
    "status": true
    }
	```
[Back to the top...](#doctor-services)


## Get Patients by Doctor ID
- GET : /doctor/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the Doctor through the query param, `id_doctor`. This would be used to fetch a list of patients that the doctor is attending to
- SAMPLE URL: `https://base.com/doctor/?id_doctor=24`

- RESPONSE:

    ```json
    [
    {
        "msg": {
            "date_of_birth": "Sun, 18 Aug 2002 00:00:00 GMT",
            "first_name": "Jerry",
            "gender": "Male",
            "house_address": "House no.23 Nyame Street",
            "id_doctor": 24,
            "id_guardian": 25,
            "id_number": "GHA-009494-124",
            "id_patient": 38,
            "last_name": "Eshun ",
            "middle_name": "Kwame",
            "nationality": "Ghanaian",
            "person_image": "",
            "phone_number": "0248963578",
            "user_email": "jerryeshun@gmail.com"
        },
        "status": true
    },
    {
        "msg": {
            "date_of_birth": "Tue, 12 Jun 2001 00:00:00 GMT",
            "first_name": "Richard",
            "gender": "male",
            "house_address": "06 Ridge avenue",
            "id_doctor": 24,
            "id_guardian": 23,
            "id_number": "GHA-08006635LTF",
            "id_patient": 42,
            "last_name": "Smith",
            "middle_name": "Sanchez",
            "nationality": "Ghanaian",
            "person_image": "https://i.pinimg.com/736x/d5/e2/e1/d5e2e1879a602c81cce3f134f0386e4c--black-models-portraits.jpg",
            "phone_number": "+233243725466",
            "user_email": "rick@st.knust.edu.gh"
        },
        "status": true
    }
  ]
    ```

[Back to top](#doctor-services)


## Get number of Patients assigned to Doctor
- GET :/doctors/patients/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the Doctor through the query param, `id_doctor`. 

- SAMPLE URL: `https://base.com/doctor/patients/?id_doctor=22`

- RESPONSE:
    ```json
    {
        "number_of_patients": 2
    }
    ```

[Back to top](#doctor-services)


## Get number of Reports assigned to Doctor
- GET :/doctors/reports/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the Doctor through the query param, `id_doctor`. 

- SAMPLE URL: `https://base.com/doctor/reports/?id_doctor=22`

- RESPONSE:
    ```json
    {
        "number_of_reports": 1
    }
    ```

[Back to top](#doctor-services)


## Get number of Appointments assigned to Doctor
- GET :/doctors/appointments/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the Doctor through the query param, `id_doctor`. 

- SAMPLE URL: `https://base.com/doctor/patients/?id_doctor=22`

- RESPONSE:
    ```json
    {
        "number_of_appointments": 3
    
    ```

[Back to top](#doctor-services)