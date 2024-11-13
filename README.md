# Financial Assistance Scheme Management System

# Project Setup Guide

## Prerequisites

- PostgreSQL

- Python 3.x

- pip (Python package installer)

## 1. Setting Up the Local SQL Database on PostgreSQL

### Step 1: Install PostgreSQL

- Download PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/)

- Follow the installation instructions for your operating system.

### Step 2: Create the Database and User

- Open the PostgreSQL shell (psql) and execute the following commands:

  ```sql

  CREATE DATABASE your_database_name;

  CREATE USER your_username WITH ENCRYPTED PASSWORD 'your_password';

  GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;

  ```

### Step 3: Create the Tables

- Use the following SQL commands to create the tables and types:

  ```sql

  CREATE TYPE employment_status_enum AS ENUM ('employed', 'unemployed');

  CREATE TYPE sex_enum AS ENUM ('male', 'female');

  CREATE TYPE marital_status_enum AS ENUM ('single', 'married', 'widowed', 'divorced');

  CREATE TABLE Administrators (

      admin_id VARCHAR(36) PRIMARY KEY,

      first_name VARCHAR(50) NOT NULL,

      last_name VARCHAR(50) NOT NULL,

      email VARCHAR(100),

      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

  );

  CREATE TABLE Applicants (

      applicant_id VARCHAR(36) PRIMARY KEY,

      first_name VARCHAR(50) NOT NULL,

      last_name VARCHAR(50) NOT NULL,

      employment_status employment_status_enum,

      sex sex_enum,

      marital_status marital_status_enum,

      date_of_birth DATE,

      household JSON

  );

  CREATE TABLE Schemes (

      scheme_id VARCHAR(36) PRIMARY KEY,

      scheme_name VARCHAR(100) NOT NULL,

      description TEXT,

      criteria JSON,

      benefits JSON

  );

  CREATE TABLE Applications (

      application_id VARCHAR(36) PRIMARY KEY,

      applicant_id VARCHAR(36) REFERENCES Applicants(applicant_id),

      scheme_id VARCHAR(36) REFERENCES Schemes(scheme_id),

      application_date DATE,

      status VARCHAR(50)

  );

  ```

## 2. Setting Up the Python Environment

### Step 1: Create a Virtual Environment

- Open your terminal and navigate to the project directory.

- Create a virtual environment using the following command:

  ```bash

  python -m venv venv

  ```

### Step 2: Activate the Virtual Environment

- Activate the virtual environment:

  - **Windows**:

    ```bash

    .\venv\Scripts\activate

    ```

  - **MacOS/Linux**:

    ```bash

    source venv/bin/activate

    ```

### Step 3: Install Dependencies

- Install the required Python packages by running:

  ```bash

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

  ```python

  DATABASE = {

      'dbname': 'your_database_name',

      'user': 'your_username',

      'password': 'your_password',

      'host': 'localhost',

      'port': 5432

  }

  ```

### Step 2: Start the Flask Application

- Ensure your virtual environment is activated.

- Run the Flask application using the following command:

  ```bash

  python app.py

  ```

### Step 3: Testing the Endpoints

- Use tools like Postman to test the API endpoints.

- Import the provided Postman collection JSON to easily test all the API endpoints.

## Notes

- Ensure that PostgreSQL is running and accessible.

- Make sure all dependencies are installed and the virtual environment is activated before running the application.
