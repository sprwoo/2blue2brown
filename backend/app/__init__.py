from flask import Flask
from flask_cors import CORS
from app.routes.chat_routes import chat_bp
from app.routes.session_routes import session_bp
from app.routes.upload_routes import upload_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat_bp, url_prefix="/api")
    app.register_blueprint(session_bp, url_prefix="/api")
    app.register_blueprint(upload_bp, url_prefix="/api")

    CORS(app)

    return app
