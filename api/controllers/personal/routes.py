import json
from flask import Blueprint, request,jsonify, abort
from api.data.db import db
from flask_jwt_extended import jwt_required,current_user
from api.schemas.Schemas import PersonalSchema
from api.models.Personal import Personal

personal_bp = Blueprint('personal_bp', __name__)

@personal_bp.put('/')
@jwt_required()
def put_estudiantes():
    data = json.loads(request.data)
    schema = PersonalSchema()
    staff = schema.load(data)
    db.session.merge(staff)
    db.session.commit()
    return jsonify(data)


@personal_bp.get('/<id_staff>')
@jwt_required()
def get_staff_id(id_staff):
    id_staff = int(id_staff)
    personal_schema = PersonalSchema()
    res = []
    sql = db.select(Personal).where(Personal.idPersonal==id_staff)
    staff = db.first_or_404(sql)
    res = personal_schema.dump(staff)
    return jsonify(res)