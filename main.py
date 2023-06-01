import os
import config
from flask import Flask
from flask_cors import CORS
from api.data.db import db
from api.schemas.ma import ma
from api.auth.routes import auth_bp
from api.controllers.encuestas.routes import encuesta_bp
from api.auth.jwt import jwt

app = Flask(__name__)
#CORS
CORS(app,supports_credentials=True)
#CORS(app)

#Configuration
app.config.from_object(config.DevConfig)

#SQL
db.init_app(app)

#Marshmallow
ma.init_app(app)

#JWT
jwt.init_app(app)

#Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(encuesta_bp, url_prefix="/encuesta")

#ERROR HANDLER
@app.errorhandler(404)
def not_found(error):
    return error

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port)
