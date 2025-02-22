Project Overview:-
The Bynry Customer Service Management System is a web-based platform that allows customers to submit complaints or service requests. The submitted requests are processed by the Customer Service Team, who update the status of each request as it moves through different stages (Pending → In Progress → Resolved). Customers can log in to their profiles and track the progress of their requests in real-time.


Key Features:-
✅ Customer Portal:

Customers can submit complaints or service requests through an online form.
Customers can attach relevant documents with their requests.
Customers can log in and track the status of their requests from their profile page.

✅ Customer Service Dashboard:

Customer service representatives can view and manage all submitted requests.
Requests can be updated to different statuses: Pending, In Progress, and Resolved.
AJAX-based status updates allow real-time changes without reloading the page.
Pagination and search functionality for efficiently managing large records.


Technology Stack:-
🚀 Backend: Django (Python)
🎨 Frontend: HTML, CSS, Bootstrap
📦 Database: sqlLite3
🔄 AJAX & JavaScript: For real-time updates without page reloads


To run server py manage.py makemigrations, py manage.py migrate, py manage.py runserver

endpoints-
  For Customer Portal localhost:8000/
                             /customerService
                                            /homepage - For to display home page form 
                                            /login -  Customer Login page
                                            /customer_register -register page 


 Customer Service Dashboard localhost:8000/
                                          EmployeeService/
                                                         /getAllCustomerComplaints - fetching  all customer form requests
                                            
                                            
