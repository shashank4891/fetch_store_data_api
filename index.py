from flask import Flask
from user_routes import user_router

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up routes
app.register_blueprint(user_router, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
