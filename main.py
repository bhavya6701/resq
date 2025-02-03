from flask import Flask
from flask_cors import CORS
from config import Config
from routes import bp as responses_bp

app = Flask(__name__)

# Load the configuration from the Config class 
app.config.from_object(Config)

# Enable CORS for the entire app
CORS(app)

# Register the blueprint for emergency responses
app.register_blueprint(responses_bp)
    

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True, port=5000)
    app.run(debug=True)
