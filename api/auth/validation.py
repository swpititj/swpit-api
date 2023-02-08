import datetime
import bcrypt
from api.models.Usuarios import Usuarios
from api.auth.jwt import jwt
from flask_jwt_extended import create_access_token


def password_validation(username, password):
    try:
        usuario = Usuarios.query.filter_by(Nombre=username).first()
        if usuario == None:
            return 0
        if(bcrypt.checkpw(password.encode('utf-8'), usuario.Clave.encode('utf-8'))):
            return usuario.idusuario
        else:
            return 0
    except Exception as e:
        return 0