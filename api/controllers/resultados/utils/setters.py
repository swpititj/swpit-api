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

    dictamen.EvalNumerica = 0
    dictamen.EvalDescripctiva = ""
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = ""

    detalles.HabitoEstudio = resultadofinal
    detalles.CalifNumerica = 0
    detalles.CalifDescriptiva = ""

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

    cantidad1 = len([int(i) for i in respuestas[0] if int(i) == 0 ])
    cantidad2 = len([int(i) for i in respuestas[0] if int(i) == 1 ])
    cantidad3 = len([int(i) for i in respuestas[0] if int(i) == 2 ])
    cantidad4 = len([int(i) for i in respuestas[0] if int(i) == 3 ])
    resultado = ""
    cantidad_final =  cantidad1+cantidad2+cantidad3+cantidad4
    if cantidad3+cantidad4 > cantidad1+cantidad2:
        resultado = "Nivel Menor"
        mensaje = "Te aconsejamos cambiar tu conducta o en algun momento podrias ver lesionados tus derechos."
    else:
        resultado = "Nivel Mayor"
        mensaje = "Te aconsejamos mantener tu conducta y evitaras que en algun momento veas lesionados tus derechos."

    dictamen.EvalNumerica = 0
    dictamen.EvalDescripctiva = ""
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = mensaje

    detalles.FactorDeAcertividad = resultado
    detalles.ValorNumerico = 0

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
    if(auditivo > visual and auditivo > kinestesico): resultado = "Auditivo"
    elif(visual > auditivo and visual > kinestesico): resultado = "Visual"
    elif(kinestesico > auditivo and kinestesico > visual): resultado = "Kinestesico"
    elif(auditivo == kinestesico == visual): resultado = "Visual Auditivo Kinestesico"
    elif(visual == auditivo): resultado = "Visual Auditivo"
    elif(visual == kinestesico): resultado = "Visual Kinestisico"
    elif(auditivo == kinestesico): resultado = "Auditivo Kinestesico"

    dictamen.EvalNumerica = 0
    dictamen.EvalDescripctiva = "Visual: "+str(visual)+", Auditivo: "+str(auditivo)+", Kinestesico: "+str(kinestesico)
    dictamen.Observaciones = ""
    dictamen.Recomendaciones = ""

    detalles.Canal = resultado
    detalles.ValorNumerico = 0

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

    resultados_extensos = ["Tienes un nivel algo bajo de autoestima y se nota en la valoración que haces de ti mismo, de tu trabajo y de tu fortuna en la vida. Una de las razones por las que percibimos más las cosas negativas es que estas son más destacables que las positivas.",
    "Tu nivel de autoestima es suficiente pero más a menudo de lo que te gustaría, te falla y te abandona. ",
    "Tu nivel de autoestima es muy bueno, sabes dar a las cosas el valor que merecen, reconoces lo bueno y no te dejas amilanar fácilmente por las adversidades.",
    "Tienes un alto nivel de autoestima y mucha confianza y seguridad en ti mismo. "]

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
        if respuesta == 0: cont[0] +=1
        elif respuesta == 1: cont[1] +=1
        elif respuesta == 2: cont[2] +=1
        else: cont[3] +=1 

    max = 0
    for i in range(4):
        if cont[i] > max:
            max = i

    cantidad_final = sum(cont)
    resultado = resultados[max]
    resultado_extenso = resultados_extensos[max]

    dictamen.EvalNumerica = 0
    dictamen.EvalDescripctiva = ""
    dictamen.Observaciones = resultado_extenso
    dictamen.Recomendaciones = ""

    detalles.ValorNumerico = 0
    detalles.FactorDeAutoEstima = resultado

    return (dictamen, detalles)

def set_HoneyAlonso(respuestas):
    dictamen = Dictamenes()
    detalles = DetalleDicHA()

    #DetalleDicHA
    #   Estilo
    #   Resultado

    activo = [3,5,7,9,13,20,26,27,35,37,41,43,46,48,51,61,67,74,75,77]
    reflexivo = [10,16,18,19,28,31,32,34,36,39,42,44,49,55,58,63,65,69,70,79]
    teorico = [2,4,6,11,15,17,21,23,25,29,33,35,50,54,60,64,66,71,78,80]
    pragmatico = [1,8,12,14,22,24,30,38,40,47,52,53,56,57,59,62,68,70,73,76]

    definiciones = [
     "Busca experiencias nuevas, son de mente abierta, nada escépticos y acometen con entusiasmo las tareas nuevas. Son muy activos, piensan que hay que intentarlo todo por lo menos una vez.",
     "Antepone la reflexión a la acción y observa con detenimiento las distintas experiencias. Les gusta considerar las experiencias y observarlas desde diferentes perspectivas.",
     "Enfoque lógico de los problemas, necesitan integrar la experiencia en un marco teórico de referencia. Enfocan los problemas de forma vertical escalonada, por etapas lógicas. Tienden a ser perfeccionistas Integran los hechos en teorías coherentes.",
     "Su punto fuerte es la experimentación y la aplicación de ideas. Descubren el aspecto positivo de las nuevas ideas y aprovechan la primera oportunidad para experimentarlas. Les gusta actuar rápidamente y con seguridad con aquellas ideas y proyectos que les atraen."
    ]

    tipos = [
         "Activo",
         "Reflexivo",
         "Teorico",
         "Pragmatico"
     ]

    cont_activo = 0
    cont_refle = 0
    cont_teo = 0
    cont_prag = 0

    respuestas = respuestas[0]

    for i, r in enumerate(respuestas, start=1):
        if r == 1:
            cont_activo += activo.count(i)
            cont_refle += reflexivo.count(i)
            cont_teo += teorico.count(i)
            cont_prag += pragmatico.count(i)

    arr_cont = [cont_activo, cont_refle, cont_teo, cont_prag]
    maximo = max(arr_cont)
    resultado = ""
    estilo = ""
    for i in range(len(arr_cont)):
        if arr_cont[i] == maximo:
            resultado=resultado+" "+tipos[i]+": "+definiciones[i]
            estilo=estilo+" "+tipos[i]
            

    dictamen.EvalNumerica = 0
    dictamen.EvalDescripctiva = ""
    dictamen.Observaciones = resultado
    dictamen.Recomendaciones = ""

    detalles.Estilo = estilo
    detalles.Resultado = 0
    return (dictamen, detalles)