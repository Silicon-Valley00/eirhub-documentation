Create a virtual environment with: virtualenv your_environment_name  
Enter your virtual environment
Install all packages in requirements.txt with pip install -r requirements.txt


Password Hashing Algorithm: 
from werkzeug.security import generate_password_hash, check_password_hash		

a = generate_password_hash('1234') //generates a password hash from word		

print(a)		

check_password_hash(a,'1234') #confirms if the hash and the word are equal and returns Bool True or False		


### Naming Patterns:        
		-	API:  Use verbs to name API functions  in camelCase. Eg: createPerson, getPerson, getPersonById, deletePerson, updatePersonById.     

		- 	Models: 	UsePascalCase to name Models ending with Model for all DB ORM Models.       
         
		-   Routes: API routes should be in the format "resource/id" or "resource/"

### Defined Response Statuses:
        - 200 OK (success)
        - 400 Error (general failure)
        - 455 Error (received data invalid)
        - 404 Error (does not exist)

### Response Format:
        - Response is always JSON

        - Success:
            {
                "msg": {
                    ...
                }, 
                "status": true
            }

        - Error:
            {
                "msg": {
                    "message": "Unable to update patient",
                    "dev_messgae": "Invalid query parameters",
                    "description": "{exception}"
                },
                "status": false
            }
        
        - All forms of failure will have a status of 'false'


[Patient](#Patient )  
[Hospital](#Hospital)  
		
  





API EndPoint Routes:
# Doctor 
- **Doctor Login**			

	POST : doctor/login		

	BODY PARAMS: 	

	```json
	{
    "user_email":"baddest70@st.knust.edu.gh",
    "user_password":"WhatTheF@ckThough54321"
    }
	```

	RESPONSE:
	```json
	{
    "msg": {
        "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
        "email": "baddest70@st.knust.edu.gh",
        "first_name": "Rexford",
        "gender": "Male",
        "last_name": "Machu",
        "license_number": "8003490390",
        "middle_name": "G.O.A.T.II"
    },
    "status": true
    }
	```
- **Doctor Registration**		

	POST : doctor/signup      

    BODY PARAMS: 	

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

	RESPONSE:
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



- **Get All Doctors**		

	GET : /doctors      

    BODY PARAMS: None

	RESPONSE:
	```json
	{
    "msg": [
        {
            "date_of_birth": "https://img.com/G.O.A.T",
            "doctor_id": 20,
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
        }
    ],
    "status": true
    }
	```    

- **Update Doctor By Id**

    PUT : /doctor/doctorId

    BODY PARAMS: 	

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
    "doctor_specialties": "Clinical pharmacy",
    "gender": "Male",
    "hospital_code": "hoc01"
   
    }
	```
    RESPONSE:
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

    

- **Get Doctor By Id**		

	GET : /doctor/doctorId        

    BODY PARAMS: None

	RESPONSE:
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





# Patient 
- **Patient Login**:			

	POST : /patients/login		

	BODY PARAMS: 	

	```json
	{
    "user_email":"baddest69@st.knust.edu.gh",
    "user_password": "baddestGO@8"
    }
	```

	RESPONSE:
	```json
	{
    "msg": {
        "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
        "idDoctor": 20,
        "email": "baddest69@st.knust.edu.gh",
        "first_name": "Rexford",
        "gender": "Male",
        "guardian_id": 20,
        "id_number": "GHA-08008238HJJ",
        "last_name": "Machu",
        "middle_name": "Patient",
        "phone_number": "+233206436575"
    },
    "status": true
    }
	```
- **Patient Registration**		

	POST : /patients/signup      

    BODY PARAMS: 	

	```json
	{
    "first_name": "Peter",
    "last_name": "Gregory",
    "user_email":"greg@st.knust.edu.gh",
    "user_password": "gregy",
    "date_of_birth":"2009-12-01",
    "doctor_id": 20,
    "guardian_id": 20
    }
	```

	RESPONSE:
	```json
	{
    "msg": {
        "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
        "doctor_id": 20,
        "first_name": "Peter",
        "gender": null,
        "guardian_id": 20,
        "id_number": null,
        "last_name": "Gregory",
        "middle_name": null,
        "phone_number": null,
        "user_email": "greg@st.knust.edu.gh"
    },
    "status": true
    }
	```   

- **Get All Patients**

    GET : /patients

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
        "msg": {
            "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
            "email": "molly@st.knust.edu.gh",
            "first_name": "Molly",
            "gender": "Male",
            "house_address": "House-4",
            "idDoctor": 20,
            "idGuardian": 20,
            "idPatient": 30,
            "id_number": "GHA-00809238HJJ",
            "last_name": "Malloy",
            "middle_name": "Patient",
            "nationality": "Ghanaian",
            "person_image": "https://img.com/G.O.A.T",
            "phone_number": "+233206436575"
        },
        "status": true
    }
    ```    
- **Get Patient by ID**

    GET : /patients/`patientID`

    BODY PARAMS: None

    RESPONSE:
    ```json
  {
        "msg": {
            "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
            "email": "molly@st.knust.edu.gh",
            "first_name": "Molly",
            "gender": "Male",
            "house_address": "House-4",
            "idDoctor": 20,
            "idGuardian": 20,
            "idPatient": 30,
            "id_number": "GHA-00809238HJJ",
            "last_name": "Malloy",
            "middle_name": "Patient",
            "nationality": "Ghanaian",
            "person_image": "https://img.com/G.O.A.T",
            "phone_number": "+233206436575"
        },
        "status": true
    }

    ```
- **Delete patient**

    DELETE: /patients/`patientID`

    BODY PARAMS: None

    RESPONSE:

    ```json
    {
        "msg": {
            "email": "Jackman@gmail.com",
            "first_name": "Jerry",
            "house_address": "12 molly street",
            "id": 24,
            "idDoctor": null,
            "idGuardian": null,
            "id_number": "57849003",
            "last_name": "Jackman",
            "middle_name": "Leo",
            "nationality": "Ghanaian",
            "person_image": "https:/myImage.com"
        },
        "status": true
    }
    ```

- **Update patient details by ID**

    PUT: /patients/`patientID`

    BODY PARAMS:

    ```json
   {
        "first_name": "Pete",
        "middle_name":"Leta",
        "last_name": "Greg",
        "person_image":"https://img.com/profilePicture",
        "email":"Gregy@st.knust.edu.gh",
        "date_of_birth":"2001-07-03",
        "house_address": "12 sesame street",
        "gender":"male",
        "phone_number" : "+233265936575",
        "id_number": "GHA-08006335HJJ",
        "nationality":"Ghanaian",
        "doctor_id": 20,
        "guardian_id": 20
    }
    ```

    RESPONSE:
    ```json
    {
    "msg": {
        "email": "Gregy@st.knust.edu.gh",
        "first_name": "Pete",
        "house_address": "12 sesame street",
        "id": 34,
        "idDoctor": 20,
        "idGuardian": 20,
        "id_number": "GHA-08006335HJJ",
        "last_name": "Greg",
        "middle_name": "Leta",
        "nationality": "Ghanaian",
        "person_image": "https://img.com/profilePicture"
    },
    "status": true
    } 
    ```




# Hospital

- **Create hospital**

POST: /hospitals

BODY PARAMS: 
```json
{
    "hospital_name": "Tech Hospital",
    "location": "knust",
    "hospital_specialities": "General Consultation",
    "number_of_doctors": 260,
    "hospital_code": "pa1s",
    "phone_number": "+233987848"
}
```

RESPONSE:
```json
{
    "msg": {
        "hospital_code": "pa1s",
        "hospital_name": "Tech Hospital",
        "hospital_specialities": "General Consultation",
        "location": "knust",
        "number_of_doctors": 260,
        "phone_number": "+233987848"
    },
    "status": true
}
```


- **Delete hospital by id**

DELETE: /hospitals/`idHospital`

BODY PARAMS: None

RESPONSE:
```json
{
    "msg": {
        "hospital_code": "ed1",
        "hospital_name": "Kah",
        "hospital_specialities": "Pediatrics",
        "id": 24,
        "location": "Bantama",
        "number_of_doctors": 134,
        "phone_number": "+2334739"
    },
    "status": true
}
```

- **Update hospital by id**


PUT: /hospitals/`idHospital`

BODY PARAMS:None

RESPONSE:
```json
{
    "msg": {
        "hospital_code": "pa1s",
        "hospital_name": "north suntreso Hospital",
        "hospital_specialities": "General Consultation",
        "id": 15,
        "location": "Santasi",
        "number_of_doctors": 260,
        "phone_number": "+233987848"
    },
    "status": true
}
```




- **Get all hospitals**
GET: /hospitals

BODY PARAMS:None

RESPONSE:
```json
{
     "msg": [
        {
            "hospital_code": "ede1",
            "hospital_name": "Kath",
            "hospital_specialities": "Pediatrics",
            "id": 12,
            "location": "Bantama",
            "number_of_doctors": 1234,
            "phone_number": "+2334739"
        },
        {
            "hospital_code": "ede1",
            "hospital_name": "Kath",
            "hospital_specialities": "Pediatrics",
            "id": 13,
            "location": "Bantama",
            "number_of_doctors": 1234,
            "phone_number": "+2334739"
        },
        {
            "hospital_code": "ede1",
            "hospital_name": "Kath",
            "hospital_specialities": "Pediatrics",
            "id": 14,
            "location": "Bantama",
            "number_of_doctors": 1234,
            "phone_number": "+2334739"
        },
        {
            "hospital_code": "ede1",
            "hospital_name": "Kath",
            "hospital_specialities": "Pediatrics",
            "id": 15,
            "location": "Bantama",
            "number_of_doctors": 1234,
            "phone_number": "+2334739"
        }
        ]
}
```


- **Get hospital based on id**
GET:/hospitals/`idHospital`


BODY PARAMS: None


RESPONSE:
```json
{
    "msg": {
        "hospital_code": "ede1",
        "hospital_name": "Kath",
        "hospital_specialities": "Pediatrics",
        "id": 15,
        "location": "Bantama",
        "number_of_doctors": 1234,
        "phone_number": "+2334739"
    },
    "status": true
}
```
        "weight": 33.0
    }
    }
    ```
- **Update healthdetails by ID**

    PUT: /uphealthdetails/`patientID`

    BODY PARAMS:

    ```json
    {
        "last_visit":"2002-09-08",
        "blood_group": "O",
        "bmi": "34.3",
        "blood_pressure": "34.6",
        "respiratory_rate": "Good",
        "pulse": "98.9",
        "blood_sugar":"Plenty",
        "weight": "87.9",
        "height": "99.3"
    }
    ```

    RESPONSE:
    ```json
    {
        "msg": {
                "blood_group": "O",
                "blood_pressure": 34.6,
                "blood_sugar": "Plenty",
                "bmi": 34.3,
                "height": 99.3,
                "last_visit": "Sun, 08 Sep 2002 00:00:00 GMT",
                "patient_id": 31,
                "pulse": 98.9,
                "respiratory_rate": "Good",
                "weight": 87.9
        },
        "status": true
    }
	```


# Report

- **Create report**

    POST: /report

    BODY PARAMS:
        
    ```json
    {
    "report_type":"Lab report",
    "description":"Lab report ordered by Dr.Raymond Brown",
    "uploaddate": 10/08/22
    }
    ```

    RESPONSE:

    ```json
     {
        "msg": {
            "description": "Lab report ordered by Dr.Raymond Brown",
            "idReport": 12,
            "report_type": "Lab report"
	    "uploaddate": 10/08/22
        },
        "status": true
    }

    ```


- **Get All reports**

GET: /reports

BODY PARAMS: None

RESPONSE:

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



- **Delete Report by Report ID**
    
    DELETE: /report/`idReport`

    BODY PARAMS: None



    RESPONSE:
    ```json
        "msg": {
            "description": "This report is for medication ",
            "idReport": 3,
            "report_type": "Medication"
        "uploaddate": 10/08/22
        },
        "status": true
    ```	


- **Update Report By Report ID**
PUT: /report/`idReport`

BODY PARAMS:


    ```json
	{
        "description": "This report is for medication ",
        "idReport": 3,
        "report_type": "Medication",
	    "upload_date": "10/08/22"
    }
	```

    RESPONSE:


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



- **Get Report By ID**

    GET: /report/`idReport`

    BODY PARAMS: None

    RESPONSE:

        ```json
        "msg": {
            "description": "This report is for medication ",
            "idReport": 3,
            "report_type": "Medication",
            "upload_date": "10/08/22"
        },
        "status": true
        ```


# Appointment

- **Add new appointment**
    POST: /appointment

    BODY PARAMS:
    ```json
    {
        "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
        "appointment_end_time": "09:00:00",
        "appointment_reason": "Severe abdominal pains",
        "appointment_start_time": "08:00:00",
        "appointment_status": "Pending",
        "idDoctor": 21,
        "idPatient": 31
    }
    ```

    RESPONSE:
    ```json
    {
        "msg": {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_reason": "Severe abdominal pains",
            "appointment_start_time": "08:00:00",
            "appointment_status": "Pending",
            "idAppointment": 1,
            "idDoctor": 21,
            "idPatient": 31
        },
        "status": true
    }
    ```

- **Get all appointments**
    GET: /appointments

    BODY PARAMS: None

    RESPONSE:
    ```json
    [
        {
            "msg": {
                "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
                "appointment_end_time": "09:00:00",
                "appointment_reason": "Severe abdominal pains",
                "appointment_start_time": "08:00:00",
                "appointment_status": "Pending",
                "idAppointment": 1,
                "idDoctor": 21,
                "idPatient": 31
            },
            "status": true
        },
        {
            "msg": {
                "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
                "appointment_end_time": "09:00:00",
                "appointment_reason": "Severe abdominal pains",
                "appointment_start_time": "08:00:00",
                "appointment_status": "Pending",
                "idAppointment": 2,
                "idDoctor": 21,
                "idPatient": 31
            },
            "status": true
        },
        {
            "msg": {
                "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
                "appointment_end_time": "14:00:00",
                "appointment_reason": "Severe abdominal pains",
                "appointment_start_time": "12:00:00",
                "appointment_status": "Accepted",
                "idAppointment": 2,
                "idDoctor": 21,
                "idPatient": 31
            },
            "status": true
        }
    ]
    ```

- **Get apppointment by patient ID**
    
   GET: /appointments/patients/`patientId`

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
    "msg": {
        "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
        "appointment_end_time": "09:00:00",
        "appointment_reason": "Severe abdominal pains",
        "appointment_start_time": "08:00:00",
        "appointment_status": "Pending",
        "idAppointment": 1,
        "idDoctor": 21,
        "idPatient": 31
    },
      "status": true
    }
    ```

- **Get appointment by doctor ID**
    
    GET:/appointments/doctors/`doctorId`

    BODY PARAMS: None

    RESPONSE:
    ```json
     {
        "msg": {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_reason": "Severe abdominal pains",
            "appointment_start_time": "08:00:00",
            "appointment_status": "Pending",
            "idAppointment": 1,
            "idDoctor": 21,
            "idPatient": 31
        },
        "status": true
    },
    ```

- **Update appointment status by its ID**
    PUT: /appointment/status/`id`/`status_ref_number`

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
        "msg": {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_reason": "Severe abdominal pains",
            "appointment_start_time": "08:00:00",
            "appointment_status": "Accepted",
            "idAppointment": 1,
            "idDoctor": 21,
            "idPatient": 31
        },
        "status": true
    }
    ```

- **Delete appointment by ID**
    DELETE: /appointment/`id`

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
        "msg": {
            "appointment_date": "Mon, 12 Dec 2022 00:00:00 GMT",
            "appointment_end_time": "09:00:00",
            "appointment_reason": "Severe abdominal pains",
            "appointment_start_time": "08:00:00",
            "appointment_status": "Accepted",
            "idAppointment": 1,
            "idDoctor": 21,
            "idPatient": 31
        },
        "status": true
    }
    ```
