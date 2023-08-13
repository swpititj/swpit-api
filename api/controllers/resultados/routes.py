import json
from flask import Blueprint, request, jsonify
from sqlalchemy import desc
from api.data.db import db
from api.models.Dictamenes import Dictamenes
from api.models.AplicPorEst import AplicPorEst
from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDictInvApre import DetalleDictInvApre
from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleDicHA import DetalleDicHA
from api.models.DetalleDicHE import DetalleDicHE
from flask_jwt_extended import jwt_required,current_user
from api.schemas.Schemas import AplicPorEstSchema
from api.controllers.encuestas.utils.evaluations import evaluate_survey

resultados_bp = Blueprint('resultados_bp', __name__)

@resultados_bp.post('/<id_survey>')
@jwt_required()
def resultadosta_post(id_survey):
    survey_data = json.loads(request.data)
    res = evaluate_survey(survey_data, current_user, int(id_survey))
    return jsonify(res), 200

@resultados_bp.get('/<id_survey>')
@jwt_required()
def resultadosta_get(id_survey):
    id_survey = int(id_survey)
    id_student = request.args.get('estudiante')
    if id_student == None:
        id_student = int(current_user['idUserType'])
    else:
        id_student = int(id_student)

    if id_survey == 1: # habilidades de estudio
        detalle = DetalleDicHE
    elif id_survey == 2: # test asertividad
        detalle = DetalleAsertividad
    elif id_survey == 3: # canales de apredizaje
        detalle = DetalleDictInvApre
    elif id_survey == 4: # autoestima
        detalle = DetalleAutoEstima
    elif id_survey == 5: # honey alonso
        detalle = DetalleDicHA
    else:
        return jsonify(''), 404
    
    sql = db.select(AplicPorEst)\
        .where(AplicPorEst.idEstudiante==id_student)\
        .join(Dictamenes)\
        .join(detalle)\
        .where(detalle.idEncuesta==id_survey)\
        .order_by(desc(AplicPorEst.idAplicPorEst))

    res_aplicporest = db.first_or_404(sql)
    
    return jsonify(AplicPorEstSchema().dump(res_aplicporest))


#@resultados_bp.get('/getall/<id_student>')
#@jwt_required()
#def get_all_results(id_student):
#
#    aplicPorEstSchema = AplicPorEstSchema(many=True)
#
#    res = AplicPorEst.query.filter_by(idEstudiante=6)\
#        .join(AplicPorEst.Dictamen)\
#        .join(Dictamenes.DetalleAsertividad, isouter=True)\
#        .join(Dictamenes.DetalleDicHA, isouter=True)\
#        .join(Dictamenes.DetalleDicHE, isouter=True)\
#        .join(Dictamenes.DetalleDictInvApre, isouter=True)\
#        .join(Dictamenes.DetalleAutoEstima, isouter=True)\
#            .all()
#    
#    return jsonify(aplicPorEstSchema.dump(res))