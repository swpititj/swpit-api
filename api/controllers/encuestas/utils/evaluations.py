import datetime
import json
from api.models.RespuestasEva import RespuestaEva
from api.models.Aplicaciones import Aplicaciones
from api.models.AplicPorEst import AplicPorEst
from api.models.Dictamenes import Dictamenes
from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDictInvApre import DetalleDictInvApre
from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleDictHA import DetalleDictHA
from api.models.DetalleDictHE import DetalleDictHE
from api.models.RespuestasEva import RespuestaEva
from api.schemas.Schemas import AplicPorEstSchema
from api.controllers.encuestas.utils.setters import set_HabilidadesEstudio, set_CanalesAprendizaje, set_TestAsertividad
from api.data.db import db

def evaluate_survey(survey_data, user_data):
    idSurvey = survey_data['idEncuesta']
    answers = survey_data['respuestas']
    #CHECAR TABLA APLICACIONES
    idApplication = 1
    #GUARDAR TABLA APLICPOREST
    date_time_start = datetime.datetime.fromtimestamp(survey_data['HoraInicial']/1000)
    date_time_end = datetime.datetime.fromtimestamp(survey_data['HoraFinal']/1000)

    aplic_por_est = AplicPorEst()
    aplic_por_est.FechaAplicacion = date_time_end.strftime('%Y-%m-%d')
    aplic_por_est.HoraInicio = date_time_start.strftime("%H:%M:%S")
    aplic_por_est.HoraFinal = date_time_end.strftime("%H:%M:%S")
    aplic_por_est.idEstudiante = user_data['idUser']
    aplic_por_est.idAplicacion = idApplication

    #db.session.add(aplic_por_est)
    #db.session.commit()

    idAplicPorEst = aplic_por_est.idAplicPorEst

    #GUARDAR EL DICTAMEN Y DETALLES
    # if idSurvey == 1: # habilidades de estudio
    #     (opinion, details) = set_HabilidadesEstudio(answers)
    # elif idSurvey == 2: # test asertividad
    #     (opinion, details) = set_TestAsertividad(answers)
    # elif idSurvey == 3: # canales de apredizaje
    #     (opinion, details) = set_CanalesAprendizaje(answers)
    # elif idSurvey == 4: # autoestima
    #     (opinion, details) = set_HabilidadesEstudio(answers)
    # elif idSurvey == 5: # honey alonso
    #     (opinion, details) = set_HabilidadesEstudio(answers)

    idDictamen = 1

    #GUARDANDO PREGUNTAS 
    questions_ids = db.engine.execute('SELECT p.idPregunta from preguntas p inner join seccion s on p.idSeccion = s.idSeccion where s.idEncuesta = '+ str(idSurvey) +' ORDER by p.idPregunta asc')
    questions = [row[0] for row in questions_ids]
    answers_dic = []
    for seccion in answers:
        for i in range(len(seccion)):
            answer = RespuestaEva()
            answer.idDictamen = idDictamen
            answer.idPregunta = questions[i]
            answer.Respuesta = seccion[i]
            answers_dic.append(answer)            
    
    db.session.add_all(answers_dic)
    db.session.commit()
    return True
