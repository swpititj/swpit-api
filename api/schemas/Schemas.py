from api.models.DetTiposPreg import DetTiposPreg
from api.models.Encuestas import Encuestas
from api.models.Preguntas import Preguntas
from api.models.Seccion import Seccion
from api.models.Tipos import Tipos
from api.schemas.ma import ma
from api.models.Usuarios import Usuarios
from marshmallow import fields
from api.models.UsuEstudiantes import UsuEstudiantes
from api.models.Estudiantes import Estudiantes
'''
from api.models.UsuPadres import UsuPadres
from api.models.PadresEstudiantes import PadresEstudiantes
from api.models.PadresFamilia import PadresFamilia
from api.models.Personal import Personal'''


class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuarios
    idusuario = ma.auto_field()
    Nombre = ma.auto_field()
    Correo = ma.auto_field()
    #Clave = ma.auto_field()
    #Activo = ma.auto_field()
    UsuEstudiantes

class UsuEstudiantesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuEstudiantes

class EstudiantesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Estudiantes 


class DetTiposPregSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetTiposPreg


class TiposSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tipos
    #DetTipoPreg = fields.Nested(DetTiposPregSchema, many=True)

class PreguntasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preguntas
    #TipoPregunta = fields.Nested(TiposSchema,)

class SeccionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seccion
        include_fk = True
    Preguntas = fields.Nested(PreguntasSchema,many=True)

class EncuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encuestas
    Secciones = fields.Nested(SeccionSchema,many=True)

'''
class EncuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encuestas

class UsuPadresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuPadres

class ResultadosCASchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResultadosCA

class ResultadosHESchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResultadosHE

class ResultadosTASchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResultadosTA

class PadresEstudiantesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PadresEstudiantes

class PadresFamiliaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PadresFamilia

class PersonalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Personal

        '''