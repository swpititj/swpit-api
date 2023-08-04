import json
from flask import Blueprint, render_template, request, redirect, make_response,jsonify, abort
from api.data.db import db,session, select
from flask_jwt_extended import jwt_required, get_current_user,current_user
from api.schemas.Schemas import SalonesSchema
from api.models.Estudiantes import Estudiantes
from api.models.Salones import Salones
from api.models.Carreras import Carreras
from api.controllers.encuestas.utils.evaluations import evaluate_survey

grupos_bp = Blueprint('grupos_bp', __name__)

@grupos_bp.get('/')
@jwt_required()
def get_estudiantes():
    id_professor = int(current_user['idUserType'])
    user_type = current_user['userType']

    if(user_type!="docente"): abort(401)

    salones_schema = SalonesSchema(many=True)
    res = []
    sql = db.select(Salones).where(Salones.idPersonal==id_professor).join(Carreras)
    groups = db.session.execute(sql).scalars()
    res = salones_schema.dump(groups)
    return jsonify(res)

@grupos_bp.get('/<id_group>')
@jwt_required()
def get_estudiante(id_group):
    id_professor = int(current_user['idUserType'])
    user_type = current_user['userType']
    id_group = int(id_group)

    if(user_type!="docente"): abort(401)

    salones_schema = SalonesSchema()
    res = []
    sql = db.select(Salones).where(Salones.idSalon==id_group).where(Salones.idPersonal==id_professor).join(Carreras).join(Estudiantes)
    groups = db.first_or_404(sql)
    res = salones_schema.dump(groups)
    return jsonify(res)