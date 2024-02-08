EmployeeAPI Contract Testing with Pact

This repository contains code for contract testing the EmployeeAPI using Pact-Python. Contract testing is a technique to ensure that the interactions between microservices are according to the specified contracts.

## Dependencies
- Python 3.x
- HTML/CSS: Frontend markup and styling.
- Django REST Framework: RESTful API framework for Django.
- PostgreSQL: Database management system.
- Swagger: For APIs documentation.
- pact-python: Library for contract testing.

## Setup

1. Clone the repository:

git clone https://github.com/alwaysvaishnav/NatWest_Assignment.git

2. Install dependencies:


3. Run migrations:
   
python manage.py makemigrations
python manage.py migrate

4. Start the development server:

python manage.py runserver

5. Access the application at [http://localhost:8000]

6. At the same time, run test.ipynb file for contract testing which will create pact file in the same directory.
