# Guardian-Person Services

Jump to...
- [Create guardian](#create-guardian-person)
- [Get all guardins](#get-all-guardian-persons)
- [Get guardian by ID](#get-guardian-person-by-id)
- [Update guardian by ID](#update-guardian-person-by-id)






## Create Guardian Person		
- POST : /guardian      
- BODY PARAMETERS: 	
    - Sample
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
- RESPONSE:
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
[Back to the top...](#guardian-person-services)

## Get All Guardian Persons	        	
- GET : /guardian      
- BODY PARAMETERS: None       
- RESPONSE:
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
[Back to the top...](#guardian-person-services)

## Get Guardian Person By Id
- GET: /guardian/`guardianId`
- BODY PARAMETERS:None
- RESPONSE: 
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
[Back to the top...](#guardian-person-services)

## Update Guardian Person By Id		
- PUT : /guardian/`guardianId`        
- BODY PARAMS: 
    - Sample
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
- RESPONSE:
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
[Back to the top...](#guardian-person-services)