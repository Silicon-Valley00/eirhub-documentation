# Doctor Services

Jump to...
- [Errors](#errors)
- [Doctor Signup](#doctor-signup)
- [Doctor login](#doctor-login)
- [Get all doctors](#get-all-doctors)
- [Update Doctor by ID](#update-doctor-by-id)
- [Get Doctor by ID](#get-doctor-by-id)

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
