from flask import Blueprint,jsonify, abort
from api.data.db import db
from flask_jwt_extended import jwt_required,current_user
from api.schemas.Schemas import SalonesSchema
from api.models.Estudiantes import Estudiantes
from api.models.Salones import Salones
from api.models.Carreras import Carreras

grupos_bp = Blueprint('grupos_bp', __name__)

@grupos_bp.get('/')
@jwt_required()
def get_estudiantes():
    id_professor = int(current_user['idUserType'])

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
    id_group = int(id_group)

    salones_schema = SalonesSchema()
    res = []
    sql = db.select(Salones).where(Salones.idSalon==id_group).where(Salones.idPersonal==id_professor).join(Carreras).join(Estudiantes)
    groups = db.first_or_404(sql)
    res = salones_schema.dump(groups)
    return jsonify(res)

@grupos_bp.get('/<id_group>/reporte/<id_survey>')
@jwt_required()
def get_report(id_group, id_survey):
    id_group = int(id_group)
    id_survey = int(id_survey)

    if id_survey == 1: # habilidades de estudio
        sql = 'SELECT COUNT(d.idDetalleDicHE), d.HabitoEstudio from detallediche d inner join dictamenes d2 on d.idDictamen  = d2.idDictamen  inner join aplicporest a on d2.idAplicPorEst = a.idAplicPorEst inner join estudiantes e on a.idEstudiante = e.idEstudiante  where e.idSalon = {} GROUP by d.HabitoEstudio'
    elif id_survey == 2: # test asertividad
        sql = 'SELECT COUNT(d.idDetalleAsertividad), d.FactorDeAcertividad from detalleasertividad d inner join dictamenes d2 on d.idDictamen  = d2.idDictamen  inner join aplicporest a on d2.idAplicPorEst = a.idAplicPorEst inner join estudiantes e on a.idEstudiante = e.idEstudiante  where e.idSalon = {} GROUP by d.FactorDeAcertividad'
    elif id_survey == 3: # canales de apredizaje
        sql = 'SELECT COUNT(d.idDetalleDictInvApre), d.Canal from detalledictinvapre d inner join dictamenes d2 on d.idDictamen  = d2.idDictamen  inner join aplicporest a on d2.idAplicPorEst = a.idAplicPorEst inner join estudiantes e on a.idEstudiante = e.idEstudiante  where e.idSalon = {} GROUP by d.Canal'
    elif id_survey == 4: # autoestima
        sql = 'SELECT COUNT(d.idDetalleAutoEstima), d.FactorDeAutoestima from detalleautoestima d  inner join dictamenes d2 on d.idDictamen  = d2.idDictamen  inner join aplicporest a on d2.idAplicPorEst = a.idAplicPorEst inner join estudiantes e on a.idEstudiante = e.idEstudiante  where e.idSalon = {} GROUP by d.FactorDeAutoestima'
    elif id_survey == 5: # honey alonso
        sql = 'SELECT COUNT(d.idDetalleDicHA), d.Estilo from detalledicha d inner join dictamenes d2 on d.idDictamen  = d2.idDictamen  inner join aplicporest a on d2.idAplicPorEst = a.idAplicPorEst inner join estudiantes e on a.idEstudiante = e.idEstudiante  where e.idSalon = {} GROUP by d.Estilo'
    else:
        response = jsonify({'message': 'error'})
        return response, 400

    sql = sql.format(id_group)

    res = {}
    for record in db.engine.execute(sql):
        res[record[1]] = record[0]
    
    return jsonify(res), 200