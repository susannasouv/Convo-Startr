from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# purpose: creates the application object(of class Flask)

from app import views # avoids circular references

