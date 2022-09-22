## Components 

The Doctor has 8 Components:
- [Doctor Sign Up](#Doctor-Signup)
- [Doctor Log In](#Doctor-Login)
 - [Dashboard](#Dashboard)
 - [Profile](#Profile) 
 - [Schedule](#Schedule)
 - [Reports](#Reports)
 - [Messages](#Messages) 
 - [Logout](#Logout)


## Doctor-Signup        
The Doctor creates an account for the application using first name, last name, email, password, Hospital Code.      
**APIs**:              
`/doctor/signup` service returns the doctor profile and patients linked to the doctor via appointments.

## Doctor-Login         
The doctor logs in to the doctor profile with an email and a password.      
**APIs**:       
The `/doctor/login` service returns the doctor profile and patients linked to the doctor via appointments.

## Dashboard        
The Doctor Dashboard page has three sections: 
- **Doctor Summary Dashboard**:     
    The Dashboard contains summarized information about the doctors activity in the app.            
    It shows the Number of Patients the doctor has Pending and Accepted Appointments with.      
    It shows the Number of Accepted Appointments the doctor has to deal with.       
    It shows the Number of Reports the Doctor is linked with.       
The `/doctors/stats/?id_doctor=${id_doctor}` service returns the information above.         
The `/appointments/?id_doctor=${id_doctor}&status=Accepted` returns information on appointments that are upcoming for the doctor.
     

- **Upcoming Appointments**:      
This displays the appointments accepted by the doctor sent from patients. It displays upcoming appointments the doctor has.

- **The Calendar** :        
The Calendar displays upcoming appointments set up for the doctor in the calendar.


## Profile
This section displays the professional and personal information of the doctor.      
The user can edit details and change profile picture by clicking the edit profile button.       
It used the information from the `/doctor/login` service.


## Schedule 
This component shows the pending appointments from patients that the doctor has to accept or decline.       
All pending appointments can be scheduled by the doctor clicking on an appointment in the pending appointments table and adding necessary information to schedule the appointment.      
The `/appointments/?id_doctor=${id_doctor}&status=Pending` returns information on appointments that are waiting for approval.       
The side panel shows a list of patients that have their respective appointments in the **Pending** or **Accepted** status.      


## Reports 
Doctor can upload report files from the device.         
The report upload uses a third party api from **Cloudinary** to upload the report and returns a url for storing the file link in our servers.
The `/report` service is used to post the link of the cloudinary upload into the server and delete is used to delete it.         
The side panel shows a list of patients that have their respective appointments in the **Pending** or **Accepted** status.      

## Messages 
The messages component opens an interactive section for communication via text, video and audio between doctors and patients.       
The side panel shows a list of patients that have their respective appointments in the **Pending** or **Accepted** status.      
The Messages component is powered by **CometChat**.     


## Logout       
The logout functionality clears the Store(local device storage) of all data stored for use within the app.


