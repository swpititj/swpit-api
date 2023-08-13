from flask import Blueprint, abort, jsonify, make_response, request
from flask_jwt_extended import jwt_required, create_access_token, current_user
from api.auth.validation import password_validation
from api.auth.jwt import jwt

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
                'mail': jwt_data['mail'],
                'name': jwt_data['name'],
             }
    return user

@auth_bp.post('/login')
def login():
    auth = request.form
    username = auth.get('username')
    password = auth.get('password')
    typeUser = auth.get('typeuser')

    if not username or not password or not typeUser:
        response = jsonify({'message': 'Datos incorrectos'})
        return response, 400

    response_data = password_validation(username, password, typeUser)
    
    if response_data == None:
        response = jsonify({'message':'Contraseña o Usuario es incorrecto'})
        return response, 401
       
    token = create_access_token(identity=response_data['idUser'], additional_claims=response_data)
    response_data['token'] = token

    return make_response(jsonify(response_data), 200)

@auth_bp.post('/logout')
def logout():
    response = jsonify("logout successful")
    return response

@auth_bp.get('/check')
@jwt_required()
def check():
    user = {
        "userType": current_user['userType'],
        "idUser": current_user['idUser'],
        "username": current_user['username'],
        "idUserType": current_user['idUserType'],
        "name": current_user['name'],
        "mail": current_user['mail'],
        'token': request.headers.get('Authorization').split()[1]
    }
    return make_response(jsonify(user), 200)

# @auth_bp.post('/create_users')
# @jwt_required()
# def create():
#     for i in range(50):
#         user = 'user'+str(i+1)
#         usu =Usuarios(Nombre=user, Clave='$2a$12$sbrPwUH6UsWUYzXNCJXWb.S3niJ7T55ISR5SvU//uGQzSqTwgjxau', Correo='correo'+str(i)+'@correo.com')
#         db.session.add(usu)
#         db.session.commit()
        
#         est = Estudiantes(NumeroControl='1842000'+str(i), ApellidoPaterno='ITJ', Nombre='Estudiante', Sexo='I')
#         db.session.add(est)
#         db.session.commit()
        
#         usu_est = UsuEstudiantes(idEstudiante=est.idEstudiante, idUsuario=usu.idusuario)
#         db.session.add(usu_est)
#         db.session.commit()
#         pass

#@auth_bp.post('/create')
#@jwt_required()
#def create():
#    data = json.loads(request.data)
#    nuevoUsuario = usuario_schema.load(data)
#    db.session.add(nuevoUsuario)
#    db.session.commit()
#    return jsonify({'res': 'user created'})
