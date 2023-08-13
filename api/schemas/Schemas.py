from api.models.DetTiposPreg import DetTiposPreg
from api.models.Encuestas import Encuestas
from api.models.Preguntas import Preguntas
from api.models.Seccion import Seccion
from api.models.Tipos import Tipos
from api.schemas.ma import ma
from api.models.Usuarios import Usuarios
from marshmallow import fields, post_load
from api.models.UsuEstudiantes import UsuEstudiantes
from api.models.Estudiantes import Estudiantes
from api.models.AplicPorEst import AplicPorEst
from api.models.Aplicaciones import Aplicaciones
from api.models.Dictamenes import Dictamenes
from api.models.Personal import Personal
from api.models.Salones import Salones
from api.models.Carreras import Carreras

from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDicHA import DetalleDicHA
from api.models.DetalleDicHE import DetalleDicHE
from api.models.DetalleDictInvApre import DetalleDictInvApre

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
        include_fk = True
    @post_load
    def make_user(self, data, **kwargs):
        return Estudiantes(**data)

class PersonalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Personal
        include_fk = True
    @post_load
    def make_user(self, data, **kwargs):
        return Personal(**data)

class DetTiposPregSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetTiposPreg

class TiposSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tipos
    DetTipoPreg = fields.Nested(DetTiposPregSchema, many=True)

class PreguntasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preguntas
    TipoPregunta = fields.Nested(TiposSchema,)

class SeccionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seccion
        #include_fk = True
    Preguntas = fields.Nested(PreguntasSchema,many=True)

class EncuestasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encuestas
    Secciones = fields.Nested(SeccionSchema,many=True)

class EncuestasCortasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encuestas    
    
class DetalleAutoEstimaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetalleAutoEstima
        exclude = ('idDetalleAutoEstima','ObservacionesTutor','FactorDeAutoEstima')
    FactorDeAutoestima = ma.auto_field("FactorDeAutoEstima", dump_only=True)
    ObservacionesDelTutor = ma.auto_field("ObservacionesTutor", dump_only=True)

class DetalleDictInvApreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetalleDictInvApre
        exclude = ('idDetalleDictInvApre','ObservacionesTutor')
    ObservacionesDelTutor = ma.auto_field("ObservacionesTutor", dump_only=True)

class DetalleDicHASchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetalleDicHA
        exclude = ('idDetalleDicHA','ObservacionesTutor')
    ObservacionesDelTutor = ma.auto_field("ObservacionesTutor", dump_only=True)

class DetalleDicHESchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetalleDicHE
        exclude = ('idDetalleDicHE','ObservacionesTutor', 'CalifNumerica', 'CalifDescriptiva')
    ObservacionesDelTutor = ma.auto_field("ObservacionesTutor", dump_only=True)
    CalificacionNumerica = ma.auto_field('CalifNumerica', dump_only=True)
    CalificacionDescriptiva = ma.auto_field('CalifDescriptiva', dump_only=True)

class DetalleAsertividadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DetalleAsertividad
        exclude = ('idDetalleAsertividad','ObservacionesTutor')
    ObservacionesDelTutor = ma.auto_field("ObservacionesTutor", dump_only=True)

class DictamenesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dictamenes
    DetalleAutoEstima = fields.Nested(DetalleAutoEstimaSchema, many=True)
    DetalleDictInvApre = fields.Nested(DetalleDictInvApreSchema, many=True)
    DetalleDicHA = fields.Nested(DetalleDicHASchema, many=True)
    DetalleDicHE = fields.Nested(DetalleDicHESchema, many=True)
    DetalleAsertividad = fields.Nested(DetalleAsertividadSchema, many=True)

class AplicPorEstSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AplicPorEst
    Dictamen = fields.Nested(DictamenesSchema, many=True)

class CarrerasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Carreras

class SalonesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salones
    Carrera = fields.Nested(CarrerasSchema)
    Estudiantes = fields.Nested(EstudiantesSchema, many=True)
        
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