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

encuesta_bp = Blueprint('encuesta_bp', __name__)

@encuesta_bp.post('/resultados')
@jwt_required()
def resultadosta_post():
    data = json.loads(request.data)
    resultado = ""
    if(data['id_encuesta'] == 1): resultado = set_ResultadosHE(data['respuestas'])
    elif(data['id_encuesta'] == 2): resultado = set_ResultadosTA(data['respuestas'])
    elif(data['id_encuesta'] == 3): resultado = set_ResultadosCA(data['respuestas'])
    else: return make_response(jsonify({'res': 'error'}), 404)
'''
@encuesta_bp.get('/resultados/<int:id>')
@jwt_required()
def get_resultado(current_user, id):
    if(id == 1): return get_ResultadosHE(current_user.idusuario)
    elif(id == 2): return get_ResultadosTA(current_user.idusuario)
    elif(id == 3): return get_ResultadosCA(current_user.idusuario)
    else: return make_response(jsonify({'res': 'error'}), 404)
'''
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

