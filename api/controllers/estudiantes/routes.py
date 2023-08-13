import json
from flask import Blueprint, request,jsonify, abort
from api.data.db import db
from flask_jwt_extended import jwt_required,current_user
from api.schemas.Schemas import EstudiantesSchema
from api.models.Estudiantes import Estudiantes
from api.models.Salones import Salones

estudiantes_bp = Blueprint('estudiantes_bp', __name__)

@estudiantes_bp.get('/')
@jwt_required()
def get_estudiantes():
    id_professor = int(current_user['idUserType'])
    user_type = current_user['userType']

    if(user_type!="docente"): abort(400)

    estudiantes_schema = EstudiantesSchema(many=True)
    res = []
    sql = db.select(Estudiantes).join(Salones).where(Salones.idPersonal==id_professor).where(Salones.activo==1)
    students = db.session.execute(sql).scalars()
    res = estudiantes_schema.dump(students)
    return jsonify(res)

@estudiantes_bp.put('/')
@jwt_required()
def put_estudiantes():
    data = json.loads(request.data)
    schema = EstudiantesSchema()
    student = schema.load(data)
    db.session.merge(student)
    db.session.commit()
    return jsonify(data)


@estudiantes_bp.get('/<id_student>')
@jwt_required()
def get_estudiantes_cn(id_student):
    id_student = int(id_student)
    estudiantes_schema = EstudiantesSchema()
    res = []
    sql = db.select(Estudiantes).where(Estudiantes.idEstudiante==id_student)
    student = db.first_or_404(sql)
    res = estudiantes_schema.dump(student)
    return jsonify(res)