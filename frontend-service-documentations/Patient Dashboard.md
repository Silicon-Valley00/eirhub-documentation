## Components 

The Patient has 10 Components:
 - [Patient Sign Up](#Patient-Signup)
 - [Patient Log In](#Patient-Login)
 - [Dashboard](#Dashboard)
 - [Profile](#Profile) 
 - [Schedule](#Schedule)
 - [Reports](#Reports)
 - [Messages](#Messages) 
 - [Prescriptions](#Prescriptions)
 - [Find a doctor](#Find-a-doctor)
 - [Logout](#Logout)


## Patient-Signup        
The Patient creates an account for the application using first name, last name, email, password. 
If the patient age is less than 18, a gaurdian form is provided to be filled.     
**APIs**:              
`/patient/signup` service returns the Patient profile and patients linked to the doctor via appointments.
the services used are;
- Guardian -> `/guardians`
- Patient -> `/patients/signup`
- Profile ->`/patients/${userID}`
- Health-> `/healthdetails/${userID}`
- Guardian -> `/guardian/${guardianID}`

## Patient-Login         
The Patient logs in to the Patient profile with an email and a password.      
**APIs**:       
The `/patient/login` service returns the Patient profile and patients linked to the doctor via appointments.
The services used are;
- Patient ->  `/patients/login`
-Profile ->  `/patients/${userID}`
- Health -> `/healthdetails/${userID}`
- Guardian ->  `/guardian/${guardianID}`


## Dashboard        
The Patient Dashboard page has three sections: 
- **Patient Summary Dashboard**:     
    The Dashboard contains summarized information about the doctors activity in the app.            
    It shows the health details of the patient; heart rate, temprature,blood pressure, blood glucose.      
    It shows the upcoming Appointments the patient has to attend.       
    It shows the current medications the Patient has to take.       
The `//healthdetails/${id_patient}` service returns the information above.         
The `/appointments/?id_patient=${id_patient}&accepted=true` returns information on appointments that are upcoming for the patient.
     The services used are:
- Prescriptions -> `/prescription/${userID}`
- Prescriptions -> `/prescription/${Id}`
-Accepted Appointments -> `/appointments/?id_patient=${userID}&accepted=${status}`

- **Upcoming Appointments**:      
This displays the appointments accepted by the doctor. It displays upcoming appointments the patient has.


## Profile
This section displays the professional and personal information of the Patient.      
The user can edit details and change profile picture by clicking the edit profile button.        
The services used are;
-Profile -> `/patients/${userID}`
-Health -> `/healthdetails/${userID}`
-Guardian -> `/guardian/${guardianId}`


## Schedule 
This component shows the pending appointments from the patient that the doctor has  yet to approve.       
All appointments can be requestd by the patient filling an appointment request and adding necessary information.      
The `/appointments/?id_patient=${id_patient}&status=Pending` returns information on appointments that have not yet been approved by the doctor.       
The side panel shows a calendar with days appointments have been scheduled.    
The services used are;
-Pending Appointments -> `/appointments/?id_patient=${userID}&accepted=${status}`
- Appointments -> `/appointments/`


## Reports 
Patient can downlod report files from the device.         
The `/report/<id_patient>` service is used to get the reports sent by the doctor.


## Messages    
The messages component opens an interactive section for communication via text, video and audio between doctors and patients.       
The side panel shows a list of doctors that have approved and scheduled appointments.      
The Messages component is powered by **CometChat**.  
The service used is;
-> Doctors associated with accepted appointments ->`/appointmentcometp/<patientId>`
  
 

## Prescriptions
Patient are able to view their prescription and are able to track their medications.
It uses the service `/prescription` to enter their prescriptions.
The services used are;
- Prescriptions -> `/prescription/${userID}`
- Prescriptions -> `/prescription`
- Prescriptions -> `/prescription/${Id}`
- Prescriptions -> `/prescription/${id}`


## Find a doctor
Patient is able to search for doctors based on their conditions and request appointments.
The  `/doctors` service is used to populate information on the page.
Patients are also able to filter doctors by specialty and hospital.
The service used is;
- Doctors -> `/doctors`

## Logout       
The logout functionality clears the Store(local device storage) of all data stored for use within the app.

