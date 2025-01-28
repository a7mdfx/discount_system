# Django Discount System

## Description
The **Django Discount System** is a web-based API project designed to manage user profiles, orders, discounts, and logs for auditing purposes. This project includes endpoints for:
- User management
- Order management
- Discount calculation
- Logs for system activities

It is designed to store all operations in a database and provides APIs for interaction.

---

## Features
1. **User Management**:
   - Fetch user details.
   - Track user orders and loyalty status.

2. **Order Management**:
   - Create, retrieve, update, and delete orders.
   - View order details and history.

3. **Discount System**:
   - Calculate discounts based on cart total and user loyalty.

4. **System Logs**:
   - Track user actions and system activities.
   - Query logs by user, action type, and date.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository


2.  Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3.  Install required dependencies:
pip install -r requirements.txt
Apply migrations:
python manage.py makemigrations
python manage.py migrate


4. Create a superuser (for Django admin):
python manage.py createsuperuser

5. Run the server:
python manage.py runserver



*API Endpoints*

* User Management
Get User Details:
GET /api/v1/users/{user_id}/

Get All Users:
GET /api/v1/users/

* Order Management
Get All Orders:
GET /api/v1/orders/

Create an Order:
POST /api/v1/orders/

Get Order Details:
GET /api/v1/orders/{order_id}/

Update an Order:
PUT /api/v1/orders/{order_id}/

Delete an Order:
DELETE /api/v1/orders/{order_id}/

* Discount Calculation
Calculate Discount:
POST /api/v1/cart/calculate-discount/

* System Logs
Query Logs:
GET /api/v1/logs/
Query Parameters:
user_id
action_type
from_date
to_date
page
limit


*How to Use*

Use tools like Postman or cURL to test the API endpoints.
For the admin panel, go to http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

* Requirements
Python 3.8+
Django 4.x
Django REST Framework

* Contributing
1.Fork the repository.
2.Create a new branch for your feature/fix.
3.Commit your changes.
4.Push to your fork and create a pull request.

* License
This project is licensed under the MIT License.

*Author*
[Ahmed Abdelkarim]
[ahmedsherif.kg@gmail.com]
[a7mdfx]