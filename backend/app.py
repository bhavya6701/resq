from flask import Flask
from config import Config
from routes import bp as responses_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register the blueprint for emergency responses
    app.register_blueprint(responses_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
