from api.data.db import db

def set_ResultadosHE(respuestas):
    #nuevoresultado = ResultadosHE()
    calificacion1 = sum([int(string) for string in respuestas[0]])
    calificacion2 = sum([int(string) for string in respuestas[1]])
    calificacion3 = sum([int(string) for string in respuestas[2]])

    calificacionfinal = calificacion3+calificacion2+calificacion1
    resultadoseccion1 = caliseccion(calificacion1)
    resultadoseccion2 = caliseccion(calificacion2)
    resultadoseccion3 = caliseccion(calificacion3)
    resultadofinal = califinal(calificacionfinal)

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

    return resultadofinal

def set_ResultadosTA(respuestas):
    cantidad1 = len([int(i) for i in respuestas[0] if int(i) == 1 ])
    cantidad2 = len([int(i) for i in respuestas[0] if int(i) == 2 ])
    cantidad3 = len([int(i) for i in respuestas[0] if int(i) == 3 ])
    cantidad4 = len([int(i) for i in respuestas[0] if int(i) == 4 ])
    resultado
    if cantidad3+cantidad4 > cantidad1+cantidad2:
        resultado = "Menor acertividad"
        mensaje = "Te aconsejamos cambiar tu conducta o en algun momento podrias ver lesionados tus derechos."
    else:
        resultado = "Mayor acertividad"
        mensaje = "Te aconsejamos mantener tu conducta y evitaras que en algun momento veas lesionados tus derechos."

    return resultado

def set_ResultadosCA(respuestas, id_user):
    respuestas  = [int(i) for i in respuestas[0]]
    visual = respuestas[0]+respuestas[2]+respuestas[5]+respuestas[8]+respuestas[9]+respuestas[10]+respuestas[13]
    auditivo = respuestas[1]+respuestas[4]+respuestas[11]+respuestas[14]+respuestas[16]+respuestas[20]+respuestas[22]
    kinestesico = respuestas[3]+respuestas[6]+respuestas[7]+respuestas[12]+respuestas[18]+respuestas[21]+respuestas[23]
    
    resultado = ""
    if(auditivo > visual and auditivo > kinestesico): resultado = "Auditiva"
    elif(visual > auditivo and visual > kinestesico): resultado = "Visual"
    elif(kinestesico > auditivo and kinestesico > visual): resultado = "Kinestesica"
    elif(auditivo == kinestesico == visual): resultado = "Visual Auditiva Kinestesica"
    elif(visual == auditivo): resultado = "Visual Auditiva"
    elif(visual == kinestesico): resultado = "Visual Kinestisica"
    elif(auditivo == kinestesico): resultado = "Auditiva Kinestesica"

    return resultado


def caliseccion(total):
    if total >= 20:
        return "Muy alto"
    elif total >= 19:
        return "Alto"
    elif total >= 18:
        return "Por encima del promedio"
    elif total >= 16:
        return "Promedio alto"
    elif total >= 14:
        return "Promedio"
    elif total >= 12:
        return "Promedio bajo"
    elif total >= 11:
        return "Por debajo del promedio"
    elif total >= 10:
        return "Bajo"
    else:
        return "Muy bajo"

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