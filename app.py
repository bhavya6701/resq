from flask import Flask
from flask_cors import CORS
from config import Config
from routes import bp as responses_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enable CORS for the entire app
    CORS(app)
    
    # Register the blueprint for emergency responses
    app.register_blueprint(responses_bp)
    
    return app

if __name__ == '__main__':
    # Bind to port 0.0.0.0 to allow external access
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
