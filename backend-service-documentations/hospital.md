# Hospital Services
Jump to ...
- [Create hospital](#create-hospital)
- [Delete hospital by id](#delete-hospital-by-id)
- [Update hospital by id](#update-hospital-by-id)
- [Get all hospitals](#get-all-hospitals)
- [Get hospital by id](#get-hospital-by-id)

## Create hospital

- POST: /hospital

- BODY PARAMETERS: `application/json` 
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

- RESPONSE:
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
[Back to top](#hospital-services)


## Delete hospital by id

- DELETE: /deletehospital/`idHospital`

- BODY PARAMETERS: None

- RESPONSE:
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
[Back to top](#hospital-services)

## Update hospital by id

- PUT: /updatehospital/`idHospital`

- BODY PARAMETERS:None

- RESPONSE:
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

[Back to top](#hospital-services)



## Get all hospitals
- GET: /getallhospital


- BODY PARAMETERS:None

- RESPONSE:
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
[Back to top](#hospital-services)


## Get hospital by id
- GET:/hospital/`idHospital`


- BODY PARAMETERS: None


- RESPONSE:
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


[Back to top](#hospital-services)