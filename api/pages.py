from api.auth.routes import auth_bp
from api.controllers.encuestas.routes import encuesta_bp
from api.controllers.estudiantes.routes import estudiantes_bp
from api.controllers.resultados.routes import resultados_bp
from api.controllers.grupos.routes import grupos_bp
from api.controllers.usuarios.routes import usuarios_bp

controllers = [
    {
        'dp_name': auth_bp,
        'url':'/auth',
        'user_types': ['estudiante', 'personal']
    },
    {
        'dp_name': encuesta_bp,
        'url':'/encuestas',
        'user_types': ['estudiante', 'personal']
    },
    {
        'dp_name': estudiantes_bp,
        'url':'/resultados',
        'user_types': ['estudiante', 'personal']
    },
    {
        'dp_name': resultados_bp,
        'url':'/estudiantes',
        'user_types': ['estudiante', 'personal']
    },
    {
        'dp_name': grupos_bp,
        'url':'/grupos',
        'user_types': ['estudiante', 'personal']
    },
    {
        'dp_name': usuarios_bp,
        'url':'/usuarios',
        'user_types': ['estudiante', 'personal']
    },
]