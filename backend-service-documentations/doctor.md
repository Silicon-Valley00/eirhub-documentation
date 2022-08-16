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
            "first_name": "Gaglo",
            "last_name": "Nathaniel",
            "user_email":"Nathaniel@gmail.com",
            "user_password":"Elormpassword",
            "date_of_birth":"1988-10-04",
            "hospital_code":"hoc01"
        }
        ```
- SAMPLE URL: `https://base.com/doctor/signup`          
- RESPONSE:
	```json
        {
        "msg": {
            "first_name": "Rexford",
            "last_name": "Machu",
            "license_number": "80034903",
            "middle_name": "G.O.A.T"
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
            "idDoctor": 22,
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
                "date_of_birth": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
                "doctor_id": 20,
                "doctor_ratings": 3,
                "doctor_specialties": "Gynaecology, Paediatric",
                "first_name": "Rexford",
                "gender": "Male",
                "hospital_code": "0",
                "house_address": "House-4",
                "last_name": "Machu",
                "license_number": "80034903",
                "middle_name": "G.O.A.T",
                "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
                "user_email": "baddest69@st.knust.edu.gh"
            },
            {
                "date_of_birth": "https://img.com/G.O.A.T.II",
                "doctor_id": 21,
                "doctor_ratings": 3,
                "doctor_specialties": "Gynaecology, Paediatric, General",
                "first_name": "Rexford",
                "gender": "Male",
                "hospital_code": "0",
                "house_address": "House-4",
                "last_name": "Machu",
                "license_number": "8003490390",
                "middle_name": "G.O.A.T.II",
                "person_image": "https://img.com/G.O.A.T.II",
                "user_email": "baddest70@st.knust.edu.gh"
            },
            {
                "date_of_birth": "https://hddesktopwallpapers.in/wp-content/uploads/2015/09/resting-images.jpg",
                "doctor_id": 22,
                "doctor_ratings": 4,
                "doctor_specialties": "Clinical pharmacy",
                "first_name": "Gaglo",
                "gender": "Male",
                "hospital_code": "hoc01",
                "house_address": "House-5",
                "last_name": "Nathaniel",
                "license_number": "80043267",
                "middle_name": "Elorm",
                "person_image": "https://hddesktopwallpapers.in/wp-content/uploads/2015/09/resting-images.jpg",
                "user_email": "nathaniel@gmail.com"
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
            "person_image": "https://hddesktopwallpapers.in/wp-content/uploads/2015/09/resting-images.jpg",
            "user_email": "nathaniel@gmail.com",
            "date_of_birth": "1988-10-04",
            "house_address": "House-5",
            "license_number": "80043267",
            "doctor_ratings": "4",
            "doctor_specialties": "Oncology",
            "gender": "Male",
            "hospital_code": "hoc01"
        
        }

	    ```
- SAMPLE URL: `https://base.com/doctor/21`  
- RESPONSE:
    ```json
        {
        "msg": {
            "date_of_birth": "Tue, 04 Oct 1988 00:00:00 GMT",
            "doctor_ratings": 4,
            "doctor_specialties": "Clinical pharmacy",
            "first_name": "Gaglo",
            "gender": "Male",
            "hospital_code": "hoc01",
            "house_address": "House-5",
            "idDoctor": 22,
            "last_name": "Nathaniel",
            "license_number": "80043267",
            "middle_name": "Elorm",
            "person_image": "https://hddesktopwallpapers.in/wp-content/uploads/2015/09/resting-images.jpg",
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
            "date_of_birth": "https://img.com/G.O.A.T",
            "doctor_ratings": 3,
            "doctor_specialties": "Gynaecology, Paediatric",
            "first_name": "Rexford",
            "gender": "Male",
            "hospital_code": "OAa3456",
            "house_address": "House-4",
            "last_name": "Machu",
            "license_number": "80034903",
            "middle_name": "G.O.A.T",
            "person_image": "https://img.com/G.O.A.T",
            "user_email": "baddest69@st.knust.edu.gh"
        },
        "status": true
        }
	```
[Back to the top...](#doctor-services)
