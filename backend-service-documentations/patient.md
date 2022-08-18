# Patient services
Jump to...
- [Errors](#errors)
- [Patient Registration](#patient-registration)
- [Patient Login](#patient-login)
- [Get all patients](#get-all-patients)
- [Get patient by ID](#get-patient-by-id)
- [Delete patient](#delete-patient)
- [Update patient by ID](#update-patient-details-by-id)


## Errors
All errors are of the form shown below:
```json
{
        "status": false,
        "msg":{
                "dev_messsage" : "(Actual Exception generated)",
                "message":"Connection Error: User not recorded" 
                        }
}
```
[Back to top](#patient-services)

## Patient Registration		

- POST : /patients/signup      

- BODY PARAMETERS:`application/json`
    - Sample:
	```json
	{
    "first_name": "Peter",
    "last_name": "Gregory",
    "user_email":"greg@st.knust.edu.gh",
    "user_password": "gregy",
    "date_of_birth":"2009-12-01",
    }
	```
- SAMPLE URL: `https://base.com/patients/signup`

- RESPONSE:
	```json
	{
    "msg": {
        "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
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

[Back to top](#patient-services)

## Patient Login

- POST : /patients/login		

- BODY PARAMETERS:`application/json` 	

	```json
	 {
    "user_email": "rick@st.knust.edu.gh",
    "user_password": "ricksanchez"
    }
	```
- SAMPLE URL: `https://base.com/patients/login`

- RESPONSE:
	```json
	{
    "msg": {
        "date_of_birth": "Sun, 13 Jun 2004 00:00:00 GMT",
        "first_name": "Richard",
        "gender": null,
        "guardian_id": null,
        "id_doctor": null,
        "id_number": null,
        "id_patient": 42,
        "last_name": "Smith",
        "middle_name": null,
        "phone_number": null,
        "user_email": "rick@st.knust.edu.gh"
    },
    "status": true
   }
	```

[Back to top](#patient-services)


## Get All Patients

- GET : /patients

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/patients`

- RESPONSE:

    ```json
    {
        "msg": {
            "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
            "first_name": "Molly",
            "gender": "Male",
            "house_address": "House-4",
            "id_doctor": 20,
            "id_guardian": 20,
            "id_number": "GHA-00809238HJJ",
            "id_patient": 30,
            "last_name": "Malloy",
            "middle_name": "Patient",
            "nationality": "Ghanaian",
            "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
            "phone_number": "+233206436575",
            "user_email": "molly@st.knust.edu.gh"
        },
        "status": true
    },
  
    ```    

[Back to top](#patient-services)


## Get Patient by ID

- GET : /patients/`patientID`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/patients/30`

- RESPONSE:

    ```json
   {
    "msg": {
        "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
        "first_name": "Molly",
        "gender": "Male",
        "house_address": "House-4",
        "id_doctor": 20,
        "id_guardian": 20,
        "id_number": "GHA-00809238HJJ",
        "id_patient": 30,
        "last_name": "Malloy",
        "middle_name": "Patient",
        "nationality": "Ghanaian",
        "person_image": "https://i.picsum.photos/id/992/200/300.jpg?hmac=TOD4LGE2HuM8Q68o5uzIoFvhlsBAiTJGRGHNMqeJTtI",
        "phone_number": "+233206436575",
        "user_email": "molly@st.knust.edu.gh"
    },
    "status": true
   }

    ```

[Back to top](#patient-services)


## Delete patient

- DELETE: /patients/`patientID`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/patients/24`

- RESPONSE:

    ```json
    {
        "msg": {
            "email": "Jackman@gmail.com",
            "first_name": "Jerry",
            "house_address": "12 molly street",
            "idPatient": 24,
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

[Back to top](#patient-services)


## Update patient details by ID

- PUT: /patients/`patientID`

- BODY PARAMETERS:`application/json`

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
- SAMPLE URL: `https://base.com/patients/34`

- RESPONSE:
    ```json
    {
    "msg": {
        "email": "Gregy@st.knust.edu.gh",
        "first_name": "Pete",
        "house_address": "12 sesame street",
        "id_patient": 34,
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

[Back to top](#patient-services)



