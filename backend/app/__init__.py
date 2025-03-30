from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Import and register blueprints
    from app.routes.chat_routes import chat_bp
    from app.routes.session_routes import session_bp

    app.register_blueprint(chat_bp, url_prefix="/api")
    app.register_blueprint(session_bp, url_prefix="/api")

    return app
