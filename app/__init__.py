from flask import Flask
from app.route import animal_route, employee_route
import os
from app.utils.database import db

app = Flask(__name__)

DATABASE_TYPE = os.getenv("DATABASE_TYPE")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

db.init_app(app)

app.register_blueprint(animal_route.animal_blueprint, url_prefix="/animal")
app.register_blueprint(employee_route.employee_blueprint, url_prefix="/employee")



# Define a route and its corresponding function
# @app.route('/')
# def hello():
#     return 'Hello, This is Our World!'

# # Run the Flask app
# if __name__ == '__main__':
#     app.run()