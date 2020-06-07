from functools import wraps

import requests
from flask import request, jsonify, current_app


def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'Message': 'Auth token is missing'}), 401

        headers = request.headers
        data = requests.request('GET', current_app.config.get('AUTH_URL') + '/authenticate/verify/{}'.format(token),
                                    headers=headers)
        current_user = None
        if data.status_code == 200:
            current_user = data.json()
        else:
            return jsonify({'Message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
