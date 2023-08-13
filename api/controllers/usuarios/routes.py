import json
from flask import Blueprint,jsonify, request
from api.data.db import db
from flask_jwt_extended import jwt_required
from api.models.Usuarios import Usuarios
import bcrypt

usuarios_bp = Blueprint('usuarios_bp', __name__)

@usuarios_bp.put('/')
@jwt_required()
def put_usuario():
    data = json.loads(request.data)

    user = Usuarios.query.filter_by(idusuario=data['idUser']).one_or_none()

    if bcrypt.checkpw(data['ClaveVieja'].encode('utf-8'), user.Clave.encode('utf-8')):
        if data['ClaveNueva'] != '':
            bytes = data['ClaveNueva'].encode('utf-8')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes, salt)
            user.Clave = hash
        user.Nombre = data['Nombre']
        user.Correo = data['Correo']
        db.session.commit()
    else:
        response = jsonify({'message':'La contraseña es incorrecta'})
        return response, 400

    return jsonify(data)
