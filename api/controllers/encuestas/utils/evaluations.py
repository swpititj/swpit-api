import datetime
import json
from api.models.RespuestaEva import RespuestaEva
from api.models.Aplicaciones import Aplicaciones
from api.models.AplicPorEst import AplicPorEst
from api.models.Dictamenes import Dictamenes
from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDictInvApre import DetalleDictInvApre
from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleDictHA import DetalleDictHA
from api.models.DetalleDictHE import DetalleDictHE
from api.models.Dictamenes import Dictamenes
from api.schemas.Schemas import AplicPorEstSchema
from api.controllers.encuestas.utils.setters import set_HabilidadesEstudio, set_CanalesAprendizaje, set_TestAsertividad
from api.data.db import db

def evaluate_survey(survey_data, user_data):
    idEncuesta = survey_data['idEncuesta']
    #CHECAR TABLA APLICACIONES
    idAplicacion = 1
    #CREAR TABLA APLICPOREST
    date_time_start = datetime.datetime.fromtimestamp(survey_data['HoraInicial']/1000)
    date_time_end = datetime.datetime.fromtimestamp(survey_data['HoraFinal']/1000)

    aplic_por_est = AplicPorEst()
    aplic_por_est.FechaAplicacion = date_time_end.strftime('%Y-%m-%d')
    aplic_por_est.HoraInicio = date_time_start.strftime("%H:%M:%S")
    aplic_por_est.HoraFinal = date_time_end.strftime("%H:%M:%S")
    aplic_por_est.idEstudiante = user_data['idUser']
    aplic_por_est.idAplicacion = idAplicacion

    db.session.add(aplic_por_est)
    #db.session.commit()

    #CREAR EL DICTAMEN
    if idEncuesta == 1: # habilidades de estudio
        dictamen = set_HabilidadesEstudio()
    elif idEncuesta == 2: # test asertividad
        dictamen = set_TestAsertividad()
    elif idEncuesta == 3: # canales de apredizaje
        dictamen = set_CanalesAprendizaje()
    elif idEncuesta == 4: # autoestima
        pasdictamen = set_HabilidadesEstudio()
    elif idEncuesta == 5: # honey alonso
        dictamen = set_HabilidadesEstudio() 
    #IR GUARDANDO LAS PREGUNTAS 
    #GUARDAR CALIFICACIONES
    return True
