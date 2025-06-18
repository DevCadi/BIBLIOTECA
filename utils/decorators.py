from functools import wraps
from flask import session, redirect, url_for, abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # CAMBIADO: 'tipo' → 'usuario_tipo'
            if 'usuario_tipo' not in session or session['usuario_tipo'] not in roles:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

