from flask import Flask
from models import db
from routes import api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hopeconnect.db'
app.config['JWT_SECRET_KEY'] = 'hopeconnect-secret-key'

db.init_app(app)
jwt = JWTManager(app)
app.register_blueprint(api)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)