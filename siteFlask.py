from flask import Flask

app = Flask(__name__)

@app.route("/")
def HomePage():
    return "Esse é o meu perfil Profissional"

@app.route("/contatos")
def contatos():
    return "<h1>Esses são meus contatos:</h1><p> E-mail: rafael.minski57@gmail.com </p> <p>whats: 45 984298012</p>"    

if __name__ == "__main__":
    app.run(debug=True)    