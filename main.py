from flask import Flask, render_template, request #importar o flask

app = Flask(__name__) #ativar o flask

@app.route('/') #criar uma rota
def index(): #cirar uma função
    return render_template('index.html') #renderizando os tempalit

@app.route('/resultado', methods=['POST']) #crinado uma nova rota
def resultado(): #criando uma outra função
    usuario = request.form['usuario'] #crinado uma variavel
    senha = request.form['senha'] #criando uma variavel

    if usuario != senha: # != usado para verificar a desigualdade entre dois valores
        resultado = "cadastro realizado com sucesso"
    else:
        resultado = "erro: a senha nao pode ser igual ao nome de usuario.por favor, tente novamente"

    return  render_template('index.html', resultado=resultado)



if __name__ == ('__main__'):  # Verifica se este arquivo está sendo executado diretamente
    app.run(debug=True) # Inicia o servidor de desenvolvimento do Flask com modo de depuração ativado
