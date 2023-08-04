# PROJETO --- Python Dev: Criação de Sites e Sistemas com Python ---
# site com os scripts : cdnjs

# Passo 1- importar o flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send


# Passo 2- Criar um APP
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # tunel


# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)


# Passo 3 Criar a nossa primeira pagina = primeira rota
@app.route("/")
def homepage():
    return render_template("index.html")


# Passo 4 - Roda o nosso aplicativo
socketio.run(app, host="26.178.218.54")


# websocket -> tunel que permite criar o site que esta criando e outra pessoa usando o site
