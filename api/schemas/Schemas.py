from api.models.DetTiposPreg import DetTiposPreg
from api.models.Encuestas import Encuestas
from api.models.Estudiantes import Estudiantes
from api.models.PadresEstudiantes import PadresEstudiantes
from api.models.PadresFamilia import PadresFamilia
from api.models.Personal import Personal
from api.models.Preguntas import Preguntas
from api.models.ResultadosCA import ResultadosCA
from api.models.ResultadosHE import ResultadosHE
from api.models.ResultadosTA import ResultadosTA
from api.models.Seccion import Seccion
from api.models.Tipos import Tipos
from api.models.Usuario import Usuario
from api.models.UsuEstudiantes import UsuEstudiantes
from api.models.UsuPadres import UsuPadres
from api.schemas.ma import ma


class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario

    idusuario = ma.auto_field()
    Nombre = ma.auto_field()
    Correo = ma.auto_field()
    #Clave = ma.auto_field()
    #Activo = ma.auto_field()

class UsuPadresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuPadres

class UsuEstudiantesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuEstudiantes

class DetTiposPregSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetTiposPreg

class EncuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encuestas

class EstudiantesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Estudiantes

class EncuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encuestas

class PadresEstudiantesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PadresEstudiantes

class PadresFamiliaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PadresFamilia

class PersonalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Personal

class PreguntasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preguntas

class ResultadosCASchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResultadosCA

class ResultadosHESchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResultadosHE

class ResultadosTASchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ResultadosTA

class SeccionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seccion

class TiposSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tipos

