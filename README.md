# Financial Assistance Scheme Management System Project Setup Guide

## Prerequisites

- PostgreSQL

- Python 3.x

- pip (Python package installer)

## 1. Setting Up the Local SQL Database on PostgreSQL

### Step 1: Install PostgreSQL

- Download PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/)

- Follow the installation instructions for your operating system.

### Step 2: Create the Database and User

- Open the pgAdmin4 desktop application and create a new Database with the following parameters:

```

DATABASE = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '111111',
    'host': 'localhost',
    'port': 5432
}

```

### Step 3: Create the Tables

- Use the SQL commands in SQL_Create.sql to create the tables and types using the Query Tool in pgAdmin4

## 2. Setting Up the Python Environment

### Step 1: Create a Virtual Environment

- Open your terminal and navigate to the project directory.

- Create a virtual environment using the following command:

```

  python -m venv venv

```

### Step 2: Activate the Virtual Environment

- Activate the virtual environment:

  - **Windows**:

```

    .\venv\Scripts\activate

```

### Step 3: Install Dependencies

- Install the required Python packages by running:

```

  pip install -r requirements.txt

```

  Ensure your `requirements.txt` includes all necessary packages, such as:

```

  Flask

  psycopg2-binary

```

## 3. Running the Application

### Step 1: Configure the Application

- Update the database configuration in your application code (`app.py`):

```

DATABASE = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '111111',
    'host': 'localhost',
    'port': 5432
}

```

### Step 2: Start the Flask Application

- Ensure your virtual environment is activated.

- Run the Flask application using the following command:

```

  python app.py

```

### Step 3: Testing the Endpoints

- Open another terminal to and run the client application using the following command:


```

  python client.py

```

## Notes

- Ensure that PostgreSQL is running and accessible.

- Make sure all dependencies are installed and the virtual environment is activated before running the application.

- API Documentation can be found at https://documenter.getpostman.com/view/39694783/2sAY55ZxBx
