# __init__.py located at C:\Code\flaskProject9\yourapp\main\__init__.py

from flask import Blueprint

# Initialize the Blueprint
main = Blueprint('main', __name__)

# Import the routes to associate them with the Blueprint
from yourapp.main import routes
