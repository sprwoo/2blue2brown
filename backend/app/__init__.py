from flask import Flask
from flask_cors import CORS
from app.routes.chat_routes import chat_bp
from app.routes.session_routes import session_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat_bp, url_prefix="/api")
    app.register_blueprint(session_bp, url_prefix="/api")

    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000"]}}, supports_credentials=True)

    # OR apply CORS directly to each blueprint (often more reliable)
    # CORS(chat_bp, origins=["http://localhost:3000"])
    # CORS(session_bp, origins=["http://localhost:3000"])

    return app
