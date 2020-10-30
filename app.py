from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/dayvson")
def dayvson():
    return "Dayvson"

@app.route("/menssage")
def menssagem():
    return "Esta é uma nova mensagem 2!"

if __name__ == "__main__":
    app.run()