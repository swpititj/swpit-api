import datetime
from api.models.RespuestasEva import RespuestaEva
from api.models.AplicPorEst import AplicPorEst
from api.models.Dictamenes import Dictamenes
from api.models.RespuestasEva import RespuestaEva
from api.controllers.resultados.utils.setters import set_HabilidadesEstudio, set_CanalesAprendizaje, set_TestAsertividad, set_autoestima,set_HoneyAlonso
from api.data.db import db

def evaluate_survey(survey_data, user_data, survey_id): 
    answers = survey_data['respuestas']
    #CHECAR TABLA APLICACIONES
    idApplication = 1
    #GUARDAR TABLA APLICPOREST
    date_time_start = datetime.datetime.fromtimestamp(survey_data['HoraInicio']/1000)
    date_time_end = datetime.datetime.fromtimestamp(survey_data['HoraFinal']/1000)

    aplic_por_est = AplicPorEst()
    aplic_por_est.FechaAplicacion = date_time_end.strftime('%Y-%m-%d')
    aplic_por_est.HoraInicio = date_time_start.strftime("%H:%M:%S")
    aplic_por_est.HoraFinal = date_time_end.strftime("%H:%M:%S")
    aplic_por_est.idEstudiante = user_data['idUserType']
    aplic_por_est.idAplicacion = idApplication

    db.session.add(aplic_por_est)
    db.session.commit()

    idAplicPorEst = aplic_por_est.idAplicPorEst

    dictamen = Dictamenes()
    #GUARDAR EL DICTAMEN Y DETALLES
    if survey_id == 1: # habilidades de estudio
        (dictamen, detalles) = set_HabilidadesEstudio(answers)
    elif survey_id == 2: # test asertividad
        (dictamen, detalles) = set_TestAsertividad(answers)
    elif survey_id == 3: # canales de apredizaje
        (dictamen, detalles) = set_CanalesAprendizaje(answers)
    elif survey_id == 4: # autoestima
        (dictamen, detalles) = set_autoestima(answers)
    elif survey_id == 5: # honey alonso
        (dictamen, detalles) = set_HoneyAlonso(answers)
    

    #DICTAMEN
    #    idAplicPorEst
    #    FechaAplicacion
    dictamen.idAplicPorEst = aplic_por_est.idAplicPorEst
    dictamen.FechaAplicacion = aplic_por_est.FechaAplicacion
    db.session.add(dictamen)
    db.session.commit()

    idDictamen = dictamen.idDictamen

    #Details
    #   ObservacionesTutor
    #   idDictamen
    #   idEncuesta
    detalles.idDictamen = dictamen.idDictamen
    detalles.idEncuesta = survey_id
    detalles.ObservacionesTutor = ""
    db.session.add(detalles)
    db.session.commit()


    #GUARDANDO PREGUNTAS 
    questions_ids = db.engine.execute('SELECT p.idPregunta FROM preguntas p INNER JOIN seccion s ON p.idSeccion = s.idSeccion WHERE s.idEncuesta = '+ str(survey_id) +' ORDER BY p.idPregunta asc')
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
