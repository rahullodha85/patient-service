from functools import wraps

import jwt
from flask import request, jsonify, current_app

from app.models.user import User


def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'Message': 'Auth token is missing'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id=data.get('public_id')).first()
        except:
            return jsonify({'Message': 'Token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorated