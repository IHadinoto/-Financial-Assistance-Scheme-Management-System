CREATE TYPE employment_status_enum AS ENUM('employed', 'unemployed');
CREATE TYPE sex_enum AS ENUM('male', 'female');
CREATE TYPE marital_status_enum AS ENUM('single', 'married', 'widowed', 'divorced');

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
