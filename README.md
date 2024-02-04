# Budget and Expenses API

## Overview

This API provides endpoints for managing budgets and expenses, protected by JWT authentication.


## MOdels

* Budget:
    user: String
    amount: double
    category: String


* Expenses:
    user: String
    amount: double
    category: String
    description: String
    date: String



## Endpoints

* Authentication:
    POST  /api/token/: Obtain a JWT token

* Budgets:
    GET /api/budget/: List all budgets

    POST /api/budget/: Create a new budget

    GET /api/budget/<#int:pk>/: Retrieve a specific budget

    PUT /api/budget/<#int:pk>/: Update a budget

    DELETE /api/budget/<#int:pk>/: Delete a budget

* Expenses:
    GET /api/expenses/: List all Expenses

    POST /api/expenses/: Create a new expenses

    GET /api/expenses/<#int:pk>/: Retrieve a specific expenses

    PUT /api/expenses/<#int:pk>/: Update a expenses

    DELETE /api/expenses/<#int:pk>/: Delete a expenses




## Installation

1. Clone the repository

        git clone https://github.com/EmmanuelOkorafor/task1.git

2. Create a virtual environment

        python -m venv venv
        source venv/bin/activate

3. Install dependencies
         
        pip install -r requirements.txt



## Running the Application

1. Apply migrations:
 
       python manage.py migrate

2. Create a superuser(optional):
       
       python manage.py createsuperuser

3. Start the development server:
        
       python manage.py runserver



## Usage

1. Obtain a JWT token

       curl -X POST -d "username=pearmonie&password=pearmonie" http://localhost:8000/api/token/

2. Use the token in the Authorization header for subsequent requests:

        curl -X GET -H "Authorization: Bearer your_token" http://localhost:8000/api/budget/



## Running on Different Operating Systems

Windows:

    * Follow the general installation and running instructions.
    * Ensure you have Python and Git installed for windows.

macOS:
    
    * Follow the general installation and running instructions.
    * Python and Git are typically pre-installed on macOS.

Linux:
    
    * Follow the general installation and running instructions.
    * Use your distribution's package manager to install Python and Git if needed.

