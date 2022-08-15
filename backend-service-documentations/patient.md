# Patient services
Jump to...
- [Patient Registration](#patient-registration)
- [Patient Login](#patient-login)
- [Get all patients](#get-all-patients)
- [Get patient by ID](#get-patient-by-id)
- [Delete patient](#delete-patient)
- [Update patient by ID](#update-patient-by-id)

- **Patient Registration**		

	POST : /patient/signup      

    BODY PARAMS: 	

	```
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
	```
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


- **Patient Login**:			

	POST : /patient/login		

	BODY PARAMS: 	

	```
	{
    "user_email":"baddest69@st.knust.edu.gh",
    "user_password": "baddestGO@8"
    }
	```

	RESPONSE:
	```
	{
    "msg": {
        "date_of_birth": "Tue, 01 Dec 2009 00:00:00 GMT",
        "doctor_id": 20,
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

- **Get All Patients**

    GET : /patient

    BODY PARAMS: None

    RESPONSE:

    ```
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

    GET : /patient/`patientID`

    BODY PARAMS: None

    RESPONSE:

    ```
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

    DELETE: /patient/`patientID`

    BODY PARAMS: None

    RESPONSE:

    ```
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

- **Update patient details by ID**

    PUT: /patient/`patientID`

    BODY PARAMS:

    ```
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
    ```
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




