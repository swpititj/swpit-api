import datetime
import json
from json import dumps
from flask import Blueprint, jsonify, make_response, request
from api.auth.validation import password_validation
from api.data.db import db
from api.models.Usuarios import Usuarios
from api.schemas.Schemas import UsuarioSchema
from flask_jwt_extended import jwt_required,get_jwt_identity, create_access_token


auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.post('/login')
def login():
    auth = request.form
    username = auth.get('username')
    password = auth.get('password')

    if not username:
        response_object = {"messages": 'username is missing'}
        return make_response(jsonify(response_object), 400)

    user_id = password_validation(username, password)

    if user_id == 0: return make_response(jsonify({}), 400)
    token = create_access_token(identity=user_id, expires_delta=datetime.timedelta(minutes=10))
    return make_response(jsonify({"token": token, "user":user_id}))

@auth_bp.route('/check')
@jwt_required()
def check():
    usuario_schema = UsuarioSchema()
    user_id = get_jwt_identity()
    usuario = Usuarios.query.filter_by(idusuario=user_id).first()
    return jsonify(usuario_schema.dump(usuario))

#@auth_bp.post('/create')
#@jwt_required()
#def create():
#    data = json.loads(request.data)
#    nuevoUsuario = usuario_schema.load(data)
#    db.session.add(nuevoUsuario)
#    db.session.commit()
#    return make_response(jsonify({'res': 'user created'}))