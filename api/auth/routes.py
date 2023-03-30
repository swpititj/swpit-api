import datetime
import json
from json import dumps
from flask import Blueprint, jsonify, make_response, request
from api.auth.validation import password_validation
from api.data.db import db
from api.auth.jwt import jwt
from api.models.Usuarios import Usuarios
from api.schemas.Schemas import UsuarioSchema
from flask_jwt_extended import jwt_required, create_access_token, set_access_cookies,unset_jwt_cookies, current_user, get_csrf_token, get_jwt


auth_bp = Blueprint('auth_bp', __name__)

@jwt.user_identity_loader
def user_identity_lookup(usuario):
    return usuario["idusuario"]

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user = Usuarios.query.filter_by(idusuario=identity).one_or_none()
    return UsuarioSchema().dump(user)

@auth_bp.post('/login')
def login():
    auth = request.form
    username = auth.get('username')
    password = auth.get('password')

    if not username:
        return jsonify('username is missing'), 400 

    user = password_validation(username, password)
    if user == 0: return jsonify("Wrong username or password"),401
   
    UserSchema = UsuarioSchema()
    user = UserSchema.dump(user)

    token = create_access_token(identity=user)

    user['csrf'] = get_csrf_token(token)
    
    response = make_response(jsonify(user))
    set_access_cookies(response, token)
    return response

@auth_bp.post('/logout')
def logout():
    response = jsonify("logout successful")
    unset_jwt_cookies(response)
    return response

@auth_bp.get('/check')
@jwt_required()
def check():
    jwt = get_jwt()
    current_user['csrf'] = jwt['csrf']
    return jsonify(current_user)

#@auth_bp.post('/create')
#@jwt_required()
#def create():
#    data = json.loads(request.data)
#    nuevoUsuario = usuario_schema.load(data)
#    db.session.add(nuevoUsuario)
#    db.session.commit()
#    return make_response(jsonify({'res': 'user created'}))