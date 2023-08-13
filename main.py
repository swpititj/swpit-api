import os
import config
from flask import Flask, request, jsonify
from flask_cors import CORS
from api.data.db import db
from api.schemas.ma import ma
from api.auth.jwt import jwt
from api.auth.routes import auth_bp
from api.controllers.encuestas.routes import encuesta_bp
from api.controllers.estudiantes.routes import estudiantes_bp
from api.controllers.resultados.routes import resultados_bp
from api.controllers.grupos.routes import grupos_bp
from api.controllers.usuarios.routes import usuarios_bp
from api.controllers.personal.routes import personal_bp

app = Flask(__name__)
#CORS
#CORS(app,supports_credentials=True, send_wildcard=True, origins="*")
CORS(app, supports_credentials=True)
#CORS(app)

#Configuration
app.config.from_object(config.ProdConfig)
#app.config.from_object(config.DevConfig)

#SQL
db.init_app(app)

#Marshmallow
ma.init_app(app)

#JWT
jwt.init_app(app)

#Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(encuesta_bp, url_prefix="/encuestas")
app.register_blueprint(resultados_bp, url_prefix="/resultados")
app.register_blueprint(estudiantes_bp, url_prefix="/estudiantes")
app.register_blueprint(grupos_bp, url_prefix="/grupos")
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(personal_bp, url_prefix="/personal")

#ERROR HANDLER
##@app.errorhandler(404)
##def not_found(error):
##    return error

@app.errorhandler(Exception)
def all_exception_handler(error):
    response = jsonify({'message': 'ERROR INTERNO: '+str(error)})
    return response, 500

#@app.before_request
#def middleware():
#    method = request.method 
#    path = request.path 
#    print('Hello Middleware')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port)
