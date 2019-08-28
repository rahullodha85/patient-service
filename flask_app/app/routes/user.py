import datetime
import json
import uuid

import jwt
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models.user import User

user = Blueprint('user', __name__)


@user.route('login', methods=['POST'])

def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = User.query.filter_by(user_name=username).first()
    if not user:
        return jsonify({'Message': 'Invalid username or password'})

    if check_password_hash(user.password, password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})


@user.route('', methods=['POST'])
def create_user():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    data['password'] = hashed_password
    user = User(**json.loads(json.dumps(data)))
    user.public_id = str(uuid.uuid4())
    db.session.add(user)
    db.session.commit()
    return jsonify({'Message': 'User Created!'})
