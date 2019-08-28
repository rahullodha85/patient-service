import json
import uuid

from flask import Blueprint, jsonify, request

from app import db
from app.helpers.decorators import authenticate
from app.models.patient import Patient

patient_controller = Blueprint('patient', __name__)


@patient_controller.route('', methods=['GET'])
@authenticate
def get_all_patients(current_user):
    patients = Patient.query.all()
    output = []
    if patients.__len__() > 0:
        for patient in patients:
            output.append(patient.serialize())
    return jsonify({'patients': output})


@patient_controller.route('', methods=['POST'])
@authenticate
def register_patient(current_user):
    data = request.json
    patient = Patient(**json.loads(json.dumps(data)))
    patient.public_id = str(uuid.uuid4())
    db.session.add(patient)
    db.session.commit()
    return jsonify({'Message': 'Patient {} {} was created'.format(patient.first_name,patient.last_name)})


@patient_controller.route('/<public_id>', methods=['GET'])
@authenticate
def get_patient(current_user, public_id):
    patient = Patient.query.filter_by(public_id=public_id).first()
    if not patient:
        return jsonify({'Message': 'Patient not found!'})
    return jsonify(patient.serialize())
