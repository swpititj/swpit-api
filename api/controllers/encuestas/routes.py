import json
from flask import Blueprint, render_template, request, redirect, make_response,jsonify
from api.data.db import db
from api.models.Encuestas import Encuestas
from api.models.Seccion import Seccion
from api.models.Preguntas import Preguntas
from api.models.Tipos import Tipos
#from api.schemas.Schemas import set_ResultadosHE, set_ResultadosTA, set_ResultadosCA
#from api.controllers.encuestas.utils.getters import get_ResultadosHE, get_ResultadosTA, get_ResultadosCA
from flask_jwt_extended import jwt_required, get_current_user,current_user
from api.schemas.Schemas import EncuestasSchema
from api.controllers.encuestas.utils.evaluations import evaluate_survey

encuesta_bp = Blueprint('encuesta_bp', __name__)

@encuesta_bp.post('/resultados')
@jwt_required()
def resultadosta_post():
    data = json.loads(request.data)
    res = evaluate_survey(data, current_user)
    return jsonify('error'), 404

@encuesta_bp.route('/<id>')
#@jwt_required()
def get_encuesta(id):
    encuesta_schemas = EncuestasSchema()
    encuesta = Encuestas.query.filter_by(idEncuesta=id).first()
    encuesta = encuesta_schemas.dump(encuesta)
    return jsonify(encuesta)

@encuesta_bp.route('/')
#@jwt_required()
def get_encuestas():
    encuestas_schema = EncuestasSchema(many=True)
    res = []
    encuestas = Encuestas.query.all()
    encuestas = encuestas_schema.dump(encuestas)
    return jsonify(encuestas)

