# Patient services
Jump to...
- [Errors](#errors)
- [Patient Registration](#patient-registration)
- [Patient Login](#patient-login)
- [Get all patients](#get-all-patients)
- [Get patient by ID](#get-patient-by-id)
- [Get doctor by patient ID](#get-doctor-by-patient-id)
- [Update patient by ID](#update-patient-details-by-id)
- [Delete patient](#delete-patient)




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


## Get Doctor by Patient ID

- GET : /patients/

- BODY PARAMETERS: None

- QUERY PARAMETERS: Provide the ID of the patient through the query param, `id_patient`. This would be used to fetch the current doctor the patient with the corresponding ID is seeing. 

- SAMPLE URL: `https://base.com/patients/?id_patient=38`

- RESPONSE:

    ```json
    {
        "msg": {
            "date_of_birth": "Sat, 21 Jun 1997 00:00:00 GMT",
            "doctor_ratings": 2,
            "doctor_specialties": "Dentistry",
            "first_name": "Kemi",
            "gender": "Female",
            "hospital_code": "KAT02",
            "house_address": "House-7",
            "id_doctor": 24,
            "last_name": "Otedola",
            "license_number": "80043223",
            "middle_name": "Oti",
            "person_image": "https://blackvoicenews.com/wp-content/uploads/2017/04/maxresdefault.jpg",
            "user_email": "kemi@gmail.com"
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
        "first_name": "Richard",
        "middle_name":"Sanchez",
        "last_name": "Smith",
        "person_image":"https://i.pinimg.com/736x/d5/e2/e1/d5e2e1879a602c81cce3f134f0386e4c--black-models-portraits.jpg",
        "user_email":"rick@st.knust.edu.gh",
        "date_of_birth":"2004-06-13",
        "house_address": "06 Ridge avenue",
        "gender":"male",
        "phone_number" : "+233243725466",
        "id_number": "GHA-08006635LTF",
        "nationality":"Ghanaian",
        "id_doctor": 25,
        "id_guardian": 23
    }

    ```
- SAMPLE URL: `https://base.com/patients/34`

- RESPONSE:
    ```json
    {
    "msg": {
        "date_of_birth": "Sun, 13 Jun 2004 00:00:00 GMT",
        "first_name": "Richard",
        "gender": "male",
        "house_address": "06 Ridge avenue",
        "id_doctor": 25,
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


