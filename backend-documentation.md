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

[HealthDetails](#HealthDetails )  
[Doctor](#Doctor )  
[Guardian](#Guardian-Person )  
[Patient](#Patient )  
[Prescription](#Prescription )  
[Hospital](#Hospital)  
[Report](#Report)
[Appoinment](#Appointment)   		
  





API EndPoint Routes:

# Prescription
- **Get Prescription By ID**
    GET: /prescription/`idPatient`

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
    "msg": [
        {
        "dosage": "1/x3",
        "drug_name": "Ibuprofen",
        "end_date": "2023-12-31",
        "id": 12,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-19",
        "time_of_administration": "12:23:45"
        },
        {
        "dosage": "1/x2",
        "drug_name": "trimetazol",
        "end_date": "2022-12-31",
        "id": 27,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
        },
        {
        "dosage": "1/x2",
        "drug_name": "paracetamol",
        "end_date": "2022-12-31",
        "id": 28,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
        },
        {
        "dosage": "1/x2",
        "drug_name": "contanitpol",
        "end_date": "2022-12-31",
        "id": 29,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
        }
    ],
    "status": true
    }
    ```
- **Get All Prescriptions**
     GET: /prescription 

     BODY PARAMS: None

     RESPONSE:
     ```json
    {
    "msg": [
        {
            "dosage": "1/day",
            "drug_name": "lepromax",
            "end_date": "2023-01-31",
            "id": 2,
            "last_taken_date": "2023-01-12",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "2/day",
            "drug_name": "ziprofin ",
            "end_date": "2023-01-31",
            "id": 3,
            "last_taken_date": "2023-01-12",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "1/day",
            "drug_name": "zipodex",
            "end_date": "2023-01-31",
            "id": 4,
            "last_taken_date": "0000-00-00",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "2/day",
            "drug_name": "laravel",
            "end_date": "2022-12-31",
            "id": 6,
            "last_taken_date": "2022-12-31",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        {
            "dosage": "2/day",
            "drug_name": "laravelproxin",
            "end_date": "2022-12-31",
            "id": 7,
            "last_taken_date": "2022-12-31",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        }
    ],
    "status": true
    }
     ```

- **Create A Prescription For A Patient**
    POST : /prescription

    BODY PARAMS: 
    ```json
        {
        "drug_name":"laravelS",
        "dosage":"2/day",
        "time_of_administration":"23:59:40",
        "start_date":"2022-12-31",
        "end_date":"2022-12-31",
        "last_taken_date":"2022-12-31",
        "idPatient":28
    }
    ```
    RESPONSE:
    ```json
    {
    "msg": {
        "dosage": "2/day",
        "drug_name": "laravelS",
        "end_date": "2022-12-31",
        "id": 8,
        "idPatient": 28,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
    },
    "status": true
    ```
- **Update Prescription By Prescription ID**
    PUT: /prescription/`idPrescription`

    BODY PARAMS:
    ```json
	{
    "drug_name":"laravelS",
    "dosage":"3/day",
    "time_of_administration":"23:59:40",
    "start_date":"2022-12-31",
    "end_date":"2022-12-31",
    "last_taken_date":"2022-12-31",
    "idPatient":28
    }
	```
    RESPONSE:
    ```json
    {
        "msg": {
            "dosage": "3/day",
            "drug_name": "laravelS",
            "end_date": "2022-12-31",
            "id": 8,
            "idPatient": 28,
            "last_taken_date": "2022-12-31",
            "start_date": "2022-12-31",
            "time_of_administration": "23:59:40"
        },
        "status": true
    }
    ```
- **Delete Prescription by Prescription ID**
    
    DELETE: /prescription/`idPrescription`

    BODY PARAMS: None

    RESPONSE:
    ```json
    "msg": {
        "dosage": "2/day",
        "drug_name": "laravel",
        "end_date": "2022-12-31",
        "id": 6,
        "idPatient": 28,
        "last_taken_date": "2022-12-31",
        "start_date": "2022-12-31",
        "time_of_administration": "23:59:40"
    },
    "status": true
    ```


    

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
    "first_name": "Rexford",
    "middle_name":"G.O.A.T.II",
    "last_name": "Machu",
    "person_image":"https://img.com/G.O.A.T.II",
    "user_email":"baddest70@st.knust.edu.gh",
    "user_password":"WhatTheF@ckThough54321",
    "date_of_birth":"2009-12-01",
    "house_address": "House-4",
    "doctor_ratings":3,
    "hospital_code":"OAa345609",
    "license_number":"8003490390",
    "doctor_specialties":"Gynaecology, Paediatric, General",
    "gender":"Male"

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
    "first_name": "Rexford",
    "middle_name":"G.O.A.T",
    "last_name": "Machu",
    "person_image":"https://img.com/G.O.A.T",
    "user_email":"baddest69@st.knust.edu.gh",
    "date_of_birth":"2009-12-01",
    "house_address": "House-4",
    "doctor_ratings":3,
    "hospital_code":"OAa3456",
    "license_number":"80034903",
    "doctor_specialties":"Gynaecology, Paediatric",
    "gender":"Male"
    }
	```
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

# Guardian-Person     

**Create Guardian Person**		

POST : /guardian      

BODY PARAMS: 	
```json
{
"first_name" : "Agbo",
"middle_name": "Turna",
"last_name" : "Collins",
"user_email" : "turna@gmail.com",
"date_of_birth" : "1999-12-21",
"house_address" : "12 molly street",
"phone_number" : "0244578953",
"id_number" : "GHA-009494-233",
"gender" : "Male"
}
```

RESPONSE:
```json
{
    "msg": {
        "date_of_birth": "Tue, 21 Dec 1999 00:00:00 GMT",
        "email": "turna@gmail.com",
        "first_name": "Agbo",
        "gender": "Male",
        "house_address": "12 molly street",
        "id_number": "GHA-009494-233",
        "last_name": "Collins",
        "middle_name": "Turna",
        "phone_number": "0244578953"
    },
    "status": true
}
```     


**Get All Guardian Persons**	        	

GET : /guardian      

BODY PARAMS: None       

RESPONSE:
```json
{
"msg": [
    {
        "date_of_birth": "Thu, 21 Dec 2000 00:00:00 GMT",
        "first_name": "Rexford ",
        "gender": "Male",
        "id_number": "GHA-009494-233",
        "last_name": "Machu",
        "middle_name": "Guardian",
        "phone_number": "0206436575",
        "user_email": "guardianofgalaxy@gmail.com"
    }
],
"status": true
}
``` 
- **Get Guardian Person By Id**

GET: /guardian/`guardianId`

BODY PARAMS:None

RESPONSE: 
```json
{
    "msg": {
        "date_of_birth": "Thu, 21 Dec 2000 00:00:00 GMT",
        "email": "guardianofgalaxy@gmail.com",
        "first_name": "Redford ",
        "gender": "Male",
        "id_number": "GHA-009494-233",
        "last_name": "Tahu",
        "middle_name": "Guardian",
        "phone_number": "0206436575"
    },
    "status": true
}
```    


**Update Guardian Person By Id**		

PUT : /guardian/`guardianId`        

BODY PARAMS: 	
```json
{
    "first_name" : "Maxford",
    "middle_name": "Daug",
    "last_name" : "Rechu",
    "user_email" : "Daug@gmail.com",
    "date_of_birth" : "2000-12-21",
    "house_address" : "House - 6",
    "phone_number" : "0206436575",
    "id_number" : "GHA-009494-233",
    "gender" : "Male"
}
```

RESPONSE:
```json
{
    "msg": {
        "date_of_birth": "Thu, 21 Dec 2000 00:00:00 GMT",
        "first_name": "Maxford",
        "gender": "Male",
        "house_address": "House - 6",
        "id_number": "GHA-009494-233",
        "last_name": "Rechu",
        "middle_name": "Daug",
        "phone_number": "0206436575",
        "user_email": "Daug@gmail.com"
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

# HealthDetails

- **Get health details by patient ID**

    GET: /healthdetails/`patientID`

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
        "msg": {
            "blood_group": "B",
            "blood_pressure": 34.6,
            "blood_sugar": "170",
            "bmi": 34.3,
            "height": 99.3,
            "last_visit": "Sun, 08 Sep 2002 00:00:00 GMT",
            "patient_id": 31,
            "pulse": 116.0,
            "respiratory_rate": "25",
            "temperature": 32.5,
            "weight": 87.9
        },
        "status": true
    }   
    ```

- **Update Health details**

    PUT: /healthdetails/`patientId`

    BODY PARAMS:
    ```json
     {
        "last_visit": "2002-09-08",
        "blood_group": "B",
        "bmi": "34.3",
        "blood_pressure": "34.6",
        "respiratory_rate": "116",
        "temperature":"37",
        "pulse": "98.9",
        "blood_sugar": "116",
        "weight": "87.9",
        "height": "99.3"
    } 	 
    ```

    RESPONSE:
    ```json
        {
            "msg": {
                "blood_group": "B",
                "blood_pressure": 34.6,
                "blood_sugar": "Plenty",
                "bmi": 34.3,
                "height": 99.3,
                "last_visit": "Sun, 08 Sep 2002 00:00:00 GMT",
                "patient_id": 31,
                "pulse": 98.9,
                "respiratory_rate": "Good",
                "temperature": 40.0,
                "weight": 87.9
            },
            "status": true
    }
    ```

- **Create Health Details**   

    POST: /healthdetails

    BODY PARAMS:
    ```json
    {
        "patient_id": "38",
        "last_visit": "2009-09-08",
        "blood_group": "O",
        "bmi": "40.3",
        "blood_pressure": "39.6",
        "respiratory_rate": "Good",
        "temperature": "43.0",
        "pulse": "89.9",
        "blood_sugar": "Plenty",
        "weight": "78.9",
        "height": "99.9"
    }
    ```

    RESPONSE:
    ```json
    {
        "msg": {
            "blood_group": "O",
            "blood_pressure": 39.6,
            "blood_sugar": "Plenty",
            "bmi": 40.3,
            "height": 99.9,
            "last_visit": "Tue, 08 Sep 2009 00:00:00 GMT",
            "patient_id": 38,
            "pulse": 89.9,
            "respiratory_rate": "Good",
            "temperature": 43.0,
            "weight": 78.9
        },
        "status": true
    }
    ```
- **Get all health details**

    GET: /healthdetails

    BODY PARAMS: None

    RESPONSE:
    ```json
    {
    "msg": [
        {
            "blood_group": "A",
            "blood_pressure": 56.0,
            "blood_sugar": "23",
            "bmi": 43.0,
            "height": 1.79,
            "last_visit": "Thu, 12 Jan 2023 00:00:00 GMT",
            "patient_id": 31,
            "pulse": 79.0,
            "respiratory_rate": "75",
            "weight": 25.0
        }
    ],
    "status": true
        }
    ```
- **Delete Health Details by ID**   
    DELETE: /healthdetails/`idHealthDetails`  

    BODY PARAMS: None   

    RESPONSE:
    ```json
    {
    "msg": {
        "blood_group": "A",
        "blood_pressure": 56.0,
        "blood_sugar": "23",
        "bmi": 43.0,
        "height": 1.8,
        "last_visit": "Thu, 12 Jan 2023 00:00:00 GMT",
        "patient_id": 30,
        "pulse": 79.0,
        "respiratory_rate": "75",
        "weight": 25.0
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
