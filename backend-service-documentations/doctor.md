# Doctor Services

Jump to...
- [Errors](#errors)
- [Doctor Signup](#doctor-signup)
- [Doctor login](#doctor-login)
- [Get all doctors](#get-all-doctors)
- [Update Doctor by ID](#update-doctor-by-id)
- [Get Doctor by ID](#get-doctor-by-id)
- [Get patients by Doctor ID](#get-patients-by-doctor-id)
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
            "last_name": "Cumberbatch",
            "user_email":"Sherlock@gmail.com",
            "user_password":"Sherlock.com1",
            "date_of_birth":"1991-11-12",
            "hospital_code":"RMC04",
            "id_message": ""
        }
        ```
- SAMPLE URL: `https://base.com/doctor/signup`          
- RESPONSE:
	```json
    {
    "msg": {
        "date_of_birth": "Tue, 12 Nov 1991 00:00:00 GMT",
        "first_name": "Benedict",
        "gender": null,
        "hospital_code": "RMC04",
        "hospital_name": "Ridge Medical Center",
        "id_doctor": 32,
        "id_message": null,
        "last_name": "Cumberbatch",
        "license_number": null,
        "middle_name": null,
        "person_image": "https://avatars.dicebear.com/api/bottts/$14.png",
        "user_email": "sherlock@gmail.com"
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
        "user_email":"sherlock@gmail.com",
        "user_password":"Sherlock.com1"
        }
        ```
- SAMPLE URL: `https://base.com/doctor/login`        
- RESPONSE:
    ```json
    {
    "msg": {
        "date_of_birth": "Tue, 12 Nov 1991 00:00:00 GMT",
        "first_name": "Benedict",
        "gender": null,
        "hospital_code": "RMC04",
        "id_doctor": 32,
        "id_message": null,
        "last_name": "Cumberbatch",
        "license_number": null,
        "middle_name": null,
        "person_image": "https://avatars.dicebear.com/api/bottts/$14.png",
        "user_email": "sherlock@gmail.com"
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
    "msg": {
        "doctors": [
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
            "last_name": "Machu",
            "license_number": "8003490390",
            "middle_name": "G.O.A.T.II",
            "person_image": "https://img.com/G.O.A.T.II",
            "user_email": "baddest70@st.knust.edu.gh"
        },
        {
            "date_of_birth": "Mon, 15 Feb 1999 00:00:00 GMT",
            "doctor_ratings": 3,
            "doctor_specialties": "Oncology",
            "first_name": "Gaglo",
            "gender": "Male",
            "hospital_code": "KAT02",
            "hospital_name": "Komfo Anokye Teaching Hospital",
            "house_address": "House-5",
            "id_doctor": 22,
            "last_name": "nathaniel",
            "license_number": "80043262",
            "middle_name": "Odartey",
            "person_image": "...",
            "user_email": "nathaniel@gmail.com"
        },
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
            "last_name": "Brempong",
            "license_number": "80043248",
            "middle_name": "Abena",
            "person_image": "http://res.cloudinary.com/eirhub-siliconvalley/image/upload/v1662052543/doctor_images/lkfnkpvitofadlqgxcna.jpg",
            "user_email": "janice@gmail.com"
        },
        {
            "date_of_birth": "Sat, 21 Jun 1997 00:00:00 GMT",
            "doctor_ratings": 2,
            "doctor_specialties": "Dentistry",
            "first_name": "Kemi",
            "gender": "Female",
            "hospital_code": "KAT02",
            "hospital_name": "Komfo Anokye Teaching Hospital",
            "house_address": "House-7",
            "id_doctor": 24,
            "last_name": "Otedola",
            "license_number": "80043223",
            "middle_name": "Oti",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "kemi@gmail.com"
        },
        {
            "date_of_birth": "Sun, 04 Oct 1992 00:00:00 GMT",
            "doctor_ratings": 4,
            "doctor_specialties": "Oncology",
            "first_name": "Maleek",
            "gender": "Male",
            "hospital_code": "GS07",
            "hospital_name": "",
            "house_address": "House-14",
            "id_doctor": 25,
            "last_name": "Dray",
            "license_number": "80043272",
            "middle_name": "Zumi",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "maleekd@gmail.com"
        },
        {
            "date_of_birth": "Sun, 16 Nov 1997 00:00:00 GMT",
            "doctor_ratings": 2,
            "doctor_specialties": "Pediatrics",
            "first_name": "Maleek",
            "gender": "Male",
            "hospital_code": "LHM08",
            "hospital_name": "",
            "house_address": "House-45",
            "id_doctor": 26,
            "last_name": "Dembele",
            "license_number": "80043273",
            "middle_name": "Usman",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "dembe@gmail.com"
        },
        {
            "date_of_birth": "Sat, 06 Oct 2001 00:00:00 GMT",
            "doctor_ratings": 4,
            "doctor_specialties": "Nephrology",
            "first_name": "Solace",
            "gender": "Female",
            "hospital_code": "KU03",
            "hospital_name": "",
            "house_address": "House-34",
            "id_doctor": 27,
            "last_name": "Bamfi",
            "license_number": "80043268",
            "middle_name": "",
            "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
            "user_email": "solace@gmail.com"
        },
        {
            "date_of_birth": "Tue, 18 Dec 1990 00:00:00 GMT",
            "doctor_ratings": 2,
            "doctor_specialties": "General surgery",
            "first_name": "Benedict",
            "gender": "Male",
            "hospital_code": "RMC04",
            "hospital_name": "Ridge Medical Center",
            "house_address": "House no.17 Maple Avenue",
            "id_doctor": 28,
            "last_name": "Freeman",
            "license_number": "80047266",
            "middle_name": "",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "Freeman@gmail.com"
        }
    ],
    "hospitals": [
            "",
            "Komfo Anokye Teaching Hospital",
            "North Legon Hospital",
            "Ridge Medical Center"
        ],
        "specialities": [
            "Gynaecology, Paediatric, General",
            "Oncology",
            "Obstetrics",
            "Dentistry",
            "Pediatrics",
            "Nephrology",
            "General surgery"
        ]
    "status": true
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
- SAMPLE URL: `https://base.com/doctor/22`  
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
        "id_message": "",
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
- GET : /doctors/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the Doctor through the query param, `id_doctor`. This would be used to fetch a list of patients that the doctor is attending to
- SAMPLE URL: `https://base.com/doctors/?id_doctor=24`

- RESPONSE:

    ```json
   {
    "msg": [
        {
            "first_name": "Pete",
            "id_message": "",
            "id_patient": 34,
            "last_name": "Greg",
            "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI"
        },
        {
            "first_name": "Fred",
            "id_message": "",
            "id_patient": 43,
            "last_name": "Adamu",
            "person_image": null
        }
    ],
    "status": true
  }
    ```

[Back to top](#doctor-services)


## Get Statistics for Doctor Dashboard
- GET :/doctors/stats/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the Doctor through the query param, `id_doctor`. 

- SAMPLE URL: `https://base.com/doctors/stats/?id_doctor=22`

- RESPONSE:
    ```json
   {
    "msg": {
        "number of appointments": 3,
        "number of patients": 2,
        "number of reports": 4
    },
    "status": true
}
    ```

[Back to top](#doctor-services)
