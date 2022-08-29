### User Dashboard:
After registration, a user is routed to this page. Based on the user status, the user is served with a patient's dashboard or a doctor's dashboard.
These pages have their own different sunb pages to serve to the user.
## Patient Dashboard Page:  
This page is dived into three sections to display components to user. Not all pages follow this format.
-  General components and other child pages are placed in a component folder while the subpages of the 
   Dashboard are placed in their own respective folders. 
-  Imports are made to use components in the subpages. Subpages are dispalyed based on selections made by a   
   user. Some sub pages are displayed along side their child pages. This is configured in a file where displays are made based on props received. This props tell what pages are to be displayed.