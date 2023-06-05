from flask import Blueprint, jsonify, make_response, request
from flask_jwt_extended import jwt_required, create_access_token, set_access_cookies, unset_jwt_cookies, current_user, get_csrf_token
from api.auth.validation import password_validation
from api.auth.jwt import jwt
from api.data.db import db
from api.models.Usuarios import Usuarios
from api.models.UsuEstudiantes import UsuEstudiantes
from api.models.Estudiantes import Estudiantes

auth_bp = Blueprint('auth_bp', __name__)

@jwt.user_identity_loader
def user_identity_lookup(idUser):
    return idUser

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    user = { 
                'userType': jwt_data['userType'],
                'idUser': jwt_data['idUser'],
                'username': jwt_data['username'],
                'idUserType': jwt_data['idUserType'],
                'name': jwt_data['name'],
                'csrf': jwt_data['csrf']
             }
    return user

@auth_bp.post('/login')
def login():
    auth = request.form
    username = auth.get('username')
    password = auth.get('password')
    typeUser = auth.get('typeuser')

    if not username:
        return jsonify('username is missing'), 400 

    response_data = password_validation(username, password, typeUser)
    
    if response_data == None: return jsonify('Wrong username or password'),401
   
    token = create_access_token(identity=response_data['idUser'], additional_claims=response_data)
    response_data['csrf'] = get_csrf_token(token)
    
    response = jsonify(response_data)
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
    user = {
        "csrf": current_user['csrf'],
        "userType": current_user['userType'],
        "idUser": current_user['idUser'],
        "username": current_user['username'],
        "idUserType": current_user['idUserType'],
        "name": current_user['name']
    }
    return make_response(jsonify(user), 200)

@auth_bp.post('/create_users')
@jwt_required()
def create():
    for i in range(50):
        user = 'user'+str(i+1)
        usu =Usuarios(Nombre=user, Clave='$2a$12$sbrPwUH6UsWUYzXNCJXWb.S3niJ7T55ISR5SvU//uGQzSqTwgjxau', Correo='correo'+str(i)+'@correo.com')
        db.session.add(usu)
        db.session.commit()
        
        est = Estudiantes(NumeroControl='1842000'+str(i), ApellidoPaterno='ITJ', Nombre='Estudiante', Sexo='I')
        db.session.add(est)
        db.session.commit()
        
        usu_est = UsuEstudiantes(idEstudiante=est.idEstudiante, idUsuario=usu.idusuario)
        db.session.add(usu_est)
        db.session.commit()
        pass

#@auth_bp.post('/create')
#@jwt_required()
#def create():
#    data = json.loads(request.data)
#    nuevoUsuario = usuario_schema.load(data)
#    db.session.add(nuevoUsuario)
#    db.session.commit()
#    return jsonify({'res': 'user created'})
