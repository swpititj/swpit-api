from flask import Blueprint,jsonify
from api.data.db import db
from api.models.Encuestas import Encuestas
from api.schemas.Schemas import EncuestasSchema, EncuestasCortasSchema
from flask_jwt_extended import jwt_required

encuesta_bp = Blueprint('encuesta_bp', __name__)

@encuesta_bp.get('/<id_survey>')
@jwt_required()
def get_encuesta(id_survey):
    id_survey = int(id_survey)
    encuesta_schemas = EncuestasSchema()

    sql = db.select(Encuestas).where(Encuestas.idEncuesta==id_survey)
    survey = db.first_or_404(sql)

    survey = encuesta_schemas.dump(survey)
    return jsonify(survey)

@encuesta_bp.get('/')
@jwt_required()
def get_encuestas():
    encuestas_schema = EncuestasCortasSchema(many=True)
    sql = db.select(Encuestas)
    surveys = db.session.execute(sql).scalars()
    return jsonify(encuestas_schema.dump(surveys))

