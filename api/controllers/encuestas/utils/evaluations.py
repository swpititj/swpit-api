from api.models.RespuestaEva import RespuestaEva
from api.models.Aplicaciones import Aplicaciones
from api.models.AplicPorEst import AplicPorEst
from api.models.Dictamenes import Dictamenes

from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDictInvApre import DetalleDictInvApre
from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleDictHA import DetalleDictHA
from api.models.DetalleDictHE import DetalleDictHE

#from api.schemas.Schemas import 

def evaluate_survey(survey_data, user_data):
    #CHECAR TABLA APLICACIONES
    id_aplicacion = 1
    #CREAR TABLA APLICPOREST
    date_time = datetime.fromtimestamp(survey_data['HoraFinal'])
    FechaAplicacion = 0
    HoraInicio = 0
    HoraFinal = 0
    idEstudiante = 1
    idAplicacion = 1
    #CREAR EL DICTAMEN
    #IR GUARDANDO LAS PREGUNTAS 
    #GUARDAR CALIFICACIONES
    return True
