import json
from flask import Blueprint, render_template, request, redirect, make_response,jsonify
from api.data.db import db,session, select
from api.models.Encuestas import Encuestas
from api.models.Dictamenes import Dictamenes
from api.models.AplicPorEst import AplicPorEst
from api.models.Preguntas import Preguntas
from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDictInvApre import DetalleDictInvApre
from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleDicHA import DetalleDicHA
from api.models.DetalleDicHE import DetalleDicHE
from api.models.Tipos import Tipos
from flask_jwt_extended import jwt_required, get_current_user,current_user
from api.schemas.Schemas import EncuestasSchema, EncuestasCortasSchema, AplicPorEstSchema,\
DetalleAutoEstimaSchema, DetalleAsertividadSchema, DetalleDictInvApreSchema,DetalleDicHASchema, DetalleDicHESchema
from api.controllers.encuestas.utils.evaluations import evaluate_survey

encuesta_bp = Blueprint('encuesta_bp', __name__)

@encuesta_bp.post('/resultados/<id_survey>')
@jwt_required()
def resultadosta_post(id_survey):
    survey_data = json.loads(request.data)
    print(survey_data)
    res = evaluate_survey(survey_data, current_user, int(id_survey))
    return jsonify(res), 200

@encuesta_bp.get('/resultados/<survey_id>')
@jwt_required()
def resultadosta_get(survey_id):
    student_id = int(current_user['idUserType'])
    survey_id = int(survey_id)

    detalle = None
    if survey_id == 1: # habilidades de estudio
        detalle = DetalleDicHE
        detalle_schema = DetalleDicHESchema
    elif survey_id == 2: # test asertividad
        detalle = DetalleAsertividad
        detalle_schema = DetalleAsertividadSchema
    elif survey_id == 3: # canales de apredizaje
        detalle = DetalleDictInvApre
        detalle_schema = DetalleDictInvApreSchema
    elif survey_id == 4: # autoestima
        detalle = DetalleAutoEstima
        detalle_schema = DetalleAutoEstimaSchema
    elif survey_id == 5: # honey alonso
        detalle = DetalleDicHA
        detalle_schema = DetalleDicHASchema

    res = AplicPorEst.query.filter_by(idEstudiante=student_id)\
        .join(Dictamenes, Dictamenes.idAplicPorEst==AplicPorEst.idAplicPorEst)\
        .join(detalle, detalle.idDictamen==Dictamenes.idDictamen)\
        .filter_by(idEncuesta=survey_id)\
        .first()
    return jsonify(AplicPorEstSchema().dump(res))

@encuesta_bp.get('/<id>')
#@jwt_required()
def get_encuesta(id):
    encuesta_schemas = EncuestasSchema()
    encuesta = Encuestas.query.filter_by(idEncuesta=id).first()
    encuesta = encuesta_schemas.dump(encuesta)
    return jsonify(encuesta)

@encuesta_bp.get('/')
#@jwt_required()
def get_encuestas():
    encuestas_schema = EncuestasCortasSchema(many=True)
    res = []
    encuestas = Encuestas.query.all()
    encuestas = encuestas_schema.dump(encuestas)
    return jsonify(encuestas)

