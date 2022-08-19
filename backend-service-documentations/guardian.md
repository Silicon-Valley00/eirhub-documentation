# Guardian-Person Services

Jump to...
- [Errors](#errors)
- [Create guardian](#create-guardian-person)
- [Get all guardians](#get-all-guardian-persons)
- [Get guardian by ID](#get-guardian-person-by-id)
- [Update guardian by ID](#update-guardian-person-by-id)


## Errors
All errors are of the form shown below:
```json
{
    "status": false,
    "msg": {
            "dev_message": "(Actual Exception generated)",
            "message": "Error : Guardian ID does not exist"
         },
     }
```
[Back to the top...](#guardian-person-services)




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
- SAMPLE URL: `https://base.com/guardian`   

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

- SAMPLE URL: `https://base.com/guardian` 

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

- SAMPLE URL: `https://base.com/guardian/25` 

- RESPONSE: 
    ```json
  {
    "msg": {
        "date_of_birth": "Sun, 29 Jun 1986 00:00:00 GMT",
        "first_name": "Beth",
        "gender": "Female",
        "house_address": "08 Oman Street",
        "id_number": "GHA-009494-159",
        "last_name": "smith",
        "middle_name": "Nana-Yaa",
        "phone_number": "0559565489",
        "user_email": "bethsmith@gmail.com"
    },
    "status": true
   }
    ```    
[Back to the top...](#guardian-person-services)

## Update Guardian Person By Id		
- PUT : /guardian/`guardianId` 

- BODY PARAMETERS: 
    - Sample
        ```json
         {
            "first_name" : "Maxford",
            "middle_name": "Daug",
            "last_name" : "Rechu",
            "user_email" : "Rechu@gmail.com",
            "date_of_birth" : "1983-09-22",
            "house_address" : "House no. 25",
            "phone_number" : "0206445925",
            "id_number" : "GHA-009494-154",
            "gender" : "Male"
        }
        ```
- SAMPLE URL: `https://base.com/guardian/22` 

- RESPONSE:
    ```json
   {
    "msg": {
        "date_of_birth": "Thu, 22 Sep 1983 00:00:00 GMT",
        "first_name": "Maxford",
        "gender": "Male",
        "house_address": "House no. 25",
        "id_number": "GHA-009494-154",
        "last_name": "Rechu",
        "middle_name": "Daug",
        "phone_number": "0206445925",
        "user_email": "Rechu@gmail.com"
    },
    "status": true
   }
    ```    
[Back to the top...](#guardian-person-services)