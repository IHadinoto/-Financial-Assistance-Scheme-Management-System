from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor, Json

app = Flask(__name__)

# Database Configuration
DATABASE = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '111111',
    'host': 'localhost',
    'port': 5432
}

def get_db_connection():
    conn = psycopg2.connect(**DATABASE)
    return conn

# Custom Serialization Function
def serialize_model(row):
    return dict(row)

# Get all applicants
@app.route('/api/applicants', methods=['GET'])
def get_applicants():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM applicants")
    applicants = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([serialize_model(applicant) for applicant in applicants])

# Create a new applicant
@app.route('/api/applicants', methods=['POST'])
def create_applicant():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO applicants (applicant_id, first_name, last_name, employment_status, sex, marital_status, date_of_birth, household)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (data['applicant_id'], data['first_name'], data['last_name'], data['employment_status'], data['sex'], data['marital_status'], data['date_of_birth'], Json(data['household']))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 201

# Get all schemes
@app.route('/api/schemes', methods=['GET'])
def get_schemes():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM schemes")
    schemes = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([serialize_model(scheme) for scheme in schemes])

# Create a new scheme
@app.route('/api/schemes', methods=['POST'])
def create_scheme():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO schemes (scheme_id, scheme_name, description, criteria, benefits)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (data['scheme_id'], data['scheme_name'], data['description'], Json(data['criteria']), Json(data['benefits']))
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 201

# Get all schemes that an applicant is eligible for
@app.route('/api/schemes/eligible', methods=['GET'])
def get_eligible_schemes():
    applicant_id = request.args.get('applicant_id')
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT employment_status FROM applicants WHERE applicant_id = %s", (applicant_id,))
    applicant = cur.fetchone()
    if not applicant:
        cur.close()
        conn.close()
        return jsonify({'error': 'Applicant not found'}), 404
    
    employment_status = applicant['employment_status']
    marital_status = applicant['marital_status']
    
    # Fetch eligible schemes based on multiple criteria 
    cur.execute(""" SELECT * FROM schemes WHERE criteria ->> 'employment_status' = %s OR criteria ->> 'marital_status' = %s """, (employment_status, marital_status))
    eligible_schemes = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([serialize_model(scheme) for scheme in eligible_schemes])

# Get all applications
@app.route('/api/applications', methods=['GET'])
def get_applications():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM applications")
    applications = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([serialize_model(application) for application in applications])

# Create a new application
@app.route('/api/applications', methods=['POST'])
def create_application():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO applications (application_id, applicant_id, scheme_id, application_date, status)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (data['application_id'], data['applicant_id'], data['scheme_id'], data['application_date'], data['status'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(data), 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
