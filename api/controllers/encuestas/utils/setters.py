#from api.data.db import db
from api.models.Dictamenes import Dictamenes
from api.models.DetalleAsertividad import DetalleAsertividad
from api.models.DetalleDicHE import DetalleDicHE
from api.models.DetalleDictInvApre import DetalleDictInvApre
from api.models.DetalleAutoEstima import DetalleAutoEstima
from api.models.DetalleDicHA import DetalleDicHA

    #DICTAMEN
    #    EvalNumerica
    #    EvalDescripctiva
    #    Observaciones
    #    Recomendaciones
    
def set_HabilidadesEstudio(respuestas):
    dictamen = Dictamenes()
    detalles = DetalleDicHE()

    #DetalleDicHE
    #   HabitoEstudio
    #   CalifNumerica
    #   CalifDescriptiva

    calificacion1 = sum([int(string) for string in respuestas[0]])
    calificacion2 = sum([int(string) for string in respuestas[1]])
    calificacion3 = sum([int(string) for string in respuestas[2]])

    calificacionfinal = calificacion3+calificacion2+calificacion1
    resultadofinal = califinal(calificacionfinal)

    dictamen.EvalNumerica = calificacionfinal
    dictamen.EvalDescripctiva = resultadofinal
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = ""

    detalles.HabitoEstudio = ""
    detalles.CalifNumerica = calificacionfinal
    detalles.CalifDescriptiva = resultadofinal

    '''resultado = ResultadosHE.query.filter_by(idUsuario=id_user).first()
    if resultado:
        nuevoresultado.idResultadoHE = resultado.idResultadoHE
        db.session.merge(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe modifed'}))
    else:
        db.session.add(nuevoresultado)
        db.session.commit()
        return make_response(jsonify({'res': 'resultadoshe created'}))'''

    return (dictamen, detalles)

def set_TestAsertividad(respuestas):
    dictamen = Dictamenes()
    detalles = DetalleAsertividad()

    #DetalleAsertividad
    #   FactorDeAsertividad
    #   ValorNumerico

    cantidad1 = len([int(i) for i in respuestas[0] if int(i) == 1 ])
    cantidad2 = len([int(i) for i in respuestas[0] if int(i) == 2 ])
    cantidad3 = len([int(i) for i in respuestas[0] if int(i) == 3 ])
    cantidad4 = len([int(i) for i in respuestas[0] if int(i) == 4 ])
    resultado = ""
    cantidad_final =  cantidad1+cantidad2+cantidad3+cantidad4
    if cantidad3+cantidad4 > cantidad1+cantidad2:
        resultado = "Menor acertividad"
        mensaje = "Te aconsejamos cambiar tu conducta o en algun momento podrias ver lesionados tus derechos."
    else:
        resultado = "  acertividad"
        mensaje = "Te aconsejamos mantener tu conducta y evitaras que en algun momento veas lesionados tus derechos."

    dictamen.EvalNumerica = cantidad_final
    dictamen.EvalDescripctiva = resultado
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = mensaje

    detalles.FactorDeAcertividad = resultado
    detalles.ValorNumerico = cantidad_final

    return (dictamen, detalles)

def set_CanalesAprendizaje(respuestas):
    dictamen = Dictamenes()
    detalles = DetalleDictInvApre()

    #CanalesAprendizaje
    #   Canal
    #   ValorNumerico

    respuestas  = [int(i) for i in respuestas[0]]
    visual = respuestas[0]+respuestas[2]+respuestas[5]+respuestas[8]+respuestas[9]+respuestas[10]+respuestas[13]
    auditivo = respuestas[1]+respuestas[4]+respuestas[11]+respuestas[14]+respuestas[16]+respuestas[20]+respuestas[22]
    kinestesico = respuestas[3]+respuestas[6]+respuestas[7]+respuestas[12]+respuestas[18]+respuestas[21]+respuestas[23]
    cantidad_final = visual+auditivo+kinestesico

    resultado = ""
    if(auditivo > visual and auditivo > kinestesico): resultado = "Auditiva"
    elif(visual > auditivo and visual > kinestesico): resultado = "Visual"
    elif(kinestesico > auditivo and kinestesico > visual): resultado = "Kinestesica"
    elif(auditivo == kinestesico == visual): resultado = "Visual Auditiva Kinestesica"
    elif(visual == auditivo): resultado = "Visual Auditiva"
    elif(visual == kinestesico): resultado = "Visual Kinestisica"
    elif(auditivo == kinestesico): resultado = "Auditiva Kinestesica"

    dictamen.EvalNumerica = cantidad_final
    dictamen.EvalDescripctiva = resultado
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = ""

    detalles.Canal = resultado
    detalles.ValorNumerico = cantidad_final

    return (dictamen, detalles)

def califinal(total):
    if total >= 57:
        return "Muy alto"
    elif total >= 52:
        return "Alto"
    elif total >= 50:
        return "Por encima del promedio"
    elif total >= 48:
        return "Promedio alto"
    elif total >= 43:
        return "Promedio"
    elif total >= 39:
        return "Promedio bajo"
    elif total >= 37:
        return "Por debajo del promedio"
    elif total >= 34:
        return "Bajo"
    else:
        return "Muy bajo"
    
def set_autoestima(respuestas):
    dictamen = Dictamenes()
    detalles = DetalleAutoEstima()

    #DetalleAutoEstima
    #   FactorDeAutoestima
    #   ValorNumerico

    cont = [0,0,0,0]

    resultados = ["Bajo",
    "Suficiente",
    "Muy bueno",
    "Alto"]

    matriz = [
        #    1 2 3 4 5 6 7 8 9 10
            [4,3,2,1,4,3,2,1,4,3], #a
            [2,1,4,3,2,1,4,3,2,1], #b
            [1,4,3,2,1,4,3,2,1,4], #c
            [3,1,1,4,3,2,1,4,3,2]  #d
              ]
    respuestas = respuestas[0]
    for i in range(len(respuestas)):
        respuesta = matriz[respuestas[i]][i]
        if respuesta == 1: cont[0] +=1
        elif respuesta == 2: cont[1] +=1
        elif respuesta == 3: cont[2] +=1
        else: cont[3] +=1 

    max = 0
    for i in range(4):
        if cont[i] > max:
            max = i

    cantidad_final = sum(cont)
    resultado = resultados[max]

    dictamen.EvalNumerica = cantidad_final
    dictamen.EvalDescripctiva = resultado
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = ""

    detalles.ValorNumerico = cantidad_final
    detalles.FactorDeAutoEstima = resultado

    return (dictamen, detalles)

def set_HoneyAlonso(respuestas):
    dictamen = Dictamenes()
    detalles = DetalleDicHA()

    #DetalleDicHA
    #   Estilo
    #   Resultado

    #....

    dictamen.EvalNumerica = ""
    dictamen.EvalDescripctiva = ""
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = ""

    detalles.Estilo = ""
    detalles.Resultado = ""
    return (dictamen, detalles)