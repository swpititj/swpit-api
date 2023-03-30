import bcrypt
from api.models.Usuarios import Usuarios

def  password_validation(username, password):
    try:
        usuario = Usuarios.query.filter_by(Nombre=username).one_or_none()
        if usuario == None:
            return 0
        if(bcrypt.checkpw(password.encode('utf-8'), usuario.Clave.encode('utf-8'))):
            return usuario
        else:
            return 0
    except Exception as e:
        return 0