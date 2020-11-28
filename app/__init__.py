from flask import Flask

# Initializing application
app = Flask(__name__)

from app import views # Allows us to create views