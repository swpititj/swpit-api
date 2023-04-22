import bcrypt
from api.models.Usuarios import Usuarios
from api.models.Estudiantes import Estudiantes
from api.models.UsuEstudiantes import UsuEstudiantes

def password_validation(username, password, userType):
    try:
        user = Usuarios.query.filter_by(Nombre=username).one_or_none()
        if user == None:
            return None
        if bcrypt.checkpw(password.encode('utf-8'), user.Clave.encode('utf-8')):
            userStudent = UsuEstudiantes.query.filter_by(idUsuario=user.idusuario).one_or_none()
            student = Estudiantes.query.filter_by(idEstudiante=userStudent.idEstudiante).one_or_none()
            return { 
                'userType': userType,
                'idUser': user.idusuario,
                'username': user.Nombre,
                'idUserType': student.idEstudiante,
                'name': student.Nombre
             }
        else:
            return None
    except Exception as e:
        return None