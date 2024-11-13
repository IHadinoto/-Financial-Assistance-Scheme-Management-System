import requests

# URL of the Flask API
url = 'http://127.0.0.1:5000/api'

# Perform a POST request to add a new applicant
new_applicant = {
    "applicant_id": "01913b7a-4493-74b2-93f8-e684c4ca935c",
    "first_name": "James",
    "last_name": "Wong",
    "employment_status": "unemployed",
    "marital_status": "single",
    "sex": "male",
    "date_of_birth": "1990-07-01",
    "household": []
}

response = requests.post(f'{url}/applicants', json=new_applicant)
print('POST /applicants response:', response.json())

# Perform a POST request to add a another applicant
new_applicant = {
    "applicant_id": "01913b80-2c04-7f9d-86a4-497ef68cb3a0",
    "first_name": "Mary",
    "last_name": "Tan",
    "employment_status": "unemployed",
    "marital_status": "married",
    "sex": "female",
    "date_of_birth": "1984-10-06",
    "household": [
        {
          "id": "01913b88-1d4d-7152-a7ce-75796a2e8ecf",
          "first_name": "Gwen",
          "last_name": "Tan",
          "employment_status": "unemployed",
          "sex": "female",
          "date_of_birth": "2016-02-01",
          "relation": "daughter",
        },
        {
          "id": "01913b88-65c6-7255-820f-9c4dd1e5ce79",
          "first_name": "Jayden",
          "last_name": "Jayden",
          "employment_status": "unemployed",
          "sex": "male",
          "date_of_birth": "2018-03-15",
          "relation": "son",
        }
    ]
}

response = requests.post(f'{url}/applicants', json=new_applicant)
print('POST /applicants response:', response.json())

# Perform a GET request to retrieve all applicants
response = requests.get(f'{url}/applicants')
print('GET /applicants response:', response.json())

# Perform a POST request to add a new scheme
new_scheme = {
    "scheme_id": "01913b89-9a43-7163-8757-01cc254783f3",
    "scheme_name": "Retrenchment Assistance Scheme",
    "description": "Financial assistance for retrenched workers",
    "criteria": {"employment_status": "unemployed"},
    "benefits": [{"id": "01913b8b-9b12-7d2c-a1fa-ea613b802ebc", "name": "SkillsFuture Credits", "amount": 500.00}]
}

response = requests.post(f'{url}/schemes', json=new_scheme)
print('POST /schemes response:', response.json())

# Perform a GET request to retrieve all schemes
response = requests.get(f'{url}/schemes')
print('GET /schemes response:', response.json())

# Perform a GET request to retrieve eligible schemes for an applicant
applicant_id = "01913b7a-4493-74b2-93f8-e684c4ca935c"
response = requests.get(f'{url}/schemes/eligible', params={'applicant_id': applicant_id})
print(f'GET /schemes/eligible?applicant_id={applicant_id} response:', response.json())

# Perform a POST request to create a new application
new_application = {
    "application_id": "01913b90-3b43-7163-8757-01cc254783f4",
    "applicant_id": "01913b7a-4493-74b2-93f8-e684c4ca935c",
    "scheme_id": "01913b89-9a43-7163-8757-01cc254783f3",
    "application_date": "2024-11-09",
    "status": "pending"
}

response = requests.post(f'{url}/applications', json=new_application)
print('POST /applications response:', response.json())

# Perform a GET request to retrieve all applications
response = requests.get(f'{url}/applications')
print('GET /applications response:', response.json())
