import bcrypt
from api.models.Usuarios import Usuarios
from api.models.Estudiantes import Estudiantes
from api.models.Personal import Personal
from api.models.UsuEstudiantes import UsuEstudiantes
from api.models.UsuarioPersonal import UsuarioPersonal
from api.models.CargosPersonal import CargosPersonal
from api.models.Puestos import Puestos

def password_validation(username, password, userType):
    try:
        user = Usuarios.query.filter_by(Nombre=username).one_or_none()
        
        if user == None:
            return None
        if bcrypt.checkpw(password.encode('utf-8'), user.Clave.encode('utf-8')):
            
            if username == 'root':
                return { 
                    'userType': 'root',
                    'idUser': user.idusuario,
                    'username': "root",
                    'idUserType': 0,
                    'mail': user.Correo,
                    'name': 'root'
                }
            
            if userType == 'alumno':
                userStudent = UsuEstudiantes.query.filter_by(idUsuario=user.idusuario).one_or_none()
                student = Estudiantes.query.filter_by(idEstudiante=userStudent.idEstudiante).one_or_none()
                return { 
                    'userType': userType,
                    'idUser': user.idusuario,
                    'username': user.Nombre,
                    'idUserType': student.idEstudiante,
                    'mail': user.Correo,
                    'name': student.Nombre
                }
        
            if userType == 'personal':
                userStaff = UsuarioPersonal.query.filter_by(idUsuario=user.idusuario).one_or_none()
                staff = Personal.query.filter_by(idPersonal=userStaff.idPersonal).one_or_none()
                positionStaff = staff.CargosPersonal[0]
                position = Puestos.query.filter_by(idPuesto=positionStaff.idPuesto).one_or_none()

                return { 
                    'userType': position.Nombre.lower(),
                    'idUser': user.idusuario,
                    'username': user.Nombre,
                    'idUserType': staff.idPersonal,
                    'mail': user.Correo,
                    'name': staff.Nombre
                }
        else:
            return None
    except Exception as e:
        return None