from flask import Flask
from Home import home
from Geocode import geocode

app = Flask(__name__)

app.register_blueprint(home.bp)
app.register_blueprint(geocode.bp)


if __name__ == '__main__':
    app.run(debug=True)
