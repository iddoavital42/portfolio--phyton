from flask import Flask, request, jsonify, send_file
from services.patient_service import add_patient, get_all_patients, delete_patient
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Swagger setup
SWAGGER_URL = '/docs'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Clinic System API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Serve the swagger.json file
@app.route('/swagger.json')
def swagger_json():
    return send_file('swagger.json')

# Routes
@app.route('/')
def index():
    return "Welcome to the Clinic System API"

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = get_all_patients()
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient_route():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    diagnosis = data.get('diagnosis')
    add_patient(name, age, diagnosis)
    return jsonify({'message': 'Patient added successfully'})

@app.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient_route(patient_id):
    delete_patient(patient_id)
    return jsonify({'message': 'Patient deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
