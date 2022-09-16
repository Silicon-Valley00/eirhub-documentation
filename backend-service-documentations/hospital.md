# Hospital Services
Jump to ...
- [Errors](#errors)
- [Create hospital](#create-hospital)
- [Delete hospital by id](#delete-hospital-by-id)
- [Update hospital by id](#update-hospital-by-id)
- [Get all hospitals](#get-all-hospitals)
- [Get hospital by id](#get-hospital-by-id)

## Errors
All errors are of the form shown below:
```json
{
    "msg": {
        "dev_message": "(Actual Exception generated)",
        "message": "Connection error: Unable to delete hospital"
    },
    "status": false
}
```
[Back to the top...](#hospital-services)


## Create hospital

- POST: /hospital

- BODY PARAMETERS: `application/json` 
    - Sample
    ```json
    {
        "hospital_name": "Light House Mission Hospital",
        "location": "North Kaneshie",
        "hospital_specialities": "General Consultation",
        "number_of_doctors": 572,
        "hospital_code": "LHM08",
        "phone_number": "0302235710"
    }
    ```

- SAMPLE URL: `https://base.com/hospital`

- RESPONSE:
    ```json
   {
    "msg": {
        "hospital_code": "LHM08",
        "hospital_name": "Light House Mission Hospital",
        "hospital_specialities": "General Consultation",
        "id_hospital": 9,
        "location": "North Kaneshie",
        "number_of_doctors": 572,
        "phone_number": "0302235710"
    },
    "status": true
    }
    ```
[Back to top](#hospital-services)


## Delete hospital by id

- DELETE: /hospital/`idHospital`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/hospital/7`

- RESPONSE:
    ```json
   {
    "msg": {
        "hospital_code": "LHM09",
        "hospital_name": "Light House Mission Hospital",
        "hospital_specialities": "General Consultation",
        "id": 9,
        "id_hospital": 9,
        "location": "North Kaneshie",
        "number_of_doctors": 572,
        "phone_number": "0302235710"
    },
    "status": true
    }
    ```
[Back to top](#hospital-services)

## Update hospital by id

- PUT: /hospital/`idHospital`

- BODY PARAMETERS:`application/json` 
     - Sample
    ```json
   {
        "hospital_name": "North Legon Hospital",
        "location": "North Legon",
        "hospital_specialities": "General",
        "number_of_doctors": 250,
        "hospital_code": "NL05",
        "phone_number": "0596698071"
    }
    ```
- SAMPLE URL: `https://base.com/hospital/6`

- RESPONSE:
    ```json
   {
    "msg": {
        "hospital_code": "NL05",
        "hospital_name": "North Legon Hospital",
        "hospital_specialities": "General",
        "id_hospital": 5,
        "location": "North Legon",
        "number_of_doctors": 250,
        "phone_number": "0596698071"
    },
    "status": true
   }
    ```

[Back to top](#hospital-services)



## Get all hospitals
- GET: /hospital

- BODY PARAMETERS:None

- SAMPLE URL: `https://base.com/hospital/6`

- RESPONSE:
    ```json
   {
    "msg": [
        {
            "hospital_code": "KBT01",
            "hospital_name": "Korle Bu Teahing Hospital",
            "hospital_specialities": "General",
            "id_hospital": 1,
            "location": "Accra",
            "number_of_doctors": 767,
            "phone_number": "0302739510"
        },
        {
            "hospital_code": "KAT02",
            "hospital_name": "Komfo Anokye Teaching Hospital",
            "hospital_specialities": "General",
            "id_hospital": 2,
            "location": "Kumasi",
            "number_of_doctors": 485,
            "phone_number": "0556490029"
        },
        {
            "hospital_code": "KU03",
            "hospital_name": "KNUST University Hospital",
            "hospital_specialities": "General",
            "id_hospital": 3,
            "location": "Kumasi",
            "number_of_doctors": 187,
            "phone_number": "0204412599"
        }
        ]
   }
    ```
[Back to top](#hospital-services)


## Get hospital by id
- GET:/hospital/`idHospital`

- BODY PARAMETERS: None

- SAMPLE URL: `https://base.com/hospital/6`

- RESPONSE:
    ```json
  {
    "msg": {
        "hospital_code": "NM06",
        "hospital_name": "Neptune Medical Center",
        "hospital_specialities": "General",
        "id_hospital": 6,
        "location": "Accra",
        "number_of_doctors": 112,
        "phone_number": null
    },
    "status": true
    }
    ```
[Back to top](#hospital-services)