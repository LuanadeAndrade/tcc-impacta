from flask import Flask, jsonify, request, render_template, redirect
import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='impacta',
    database='bdimpacra',
)

cursor = conexao.cursor()


app = Flask(__name__)

retornar = f'SELECT * FROM curso'
cursor.execute(retornar)
resultados = cursor.fetchall()


@app.route('/')
def index():
    trazer = f'SELECT * FROM curso'
    cursor.execute(trazer)
    resultado = cursor.fetchall()
    return render_template('cadastro.html', titulo='Lista de alunos cadastrados', resultado=resultado)

@app.route('/criar', methods=['POST',])
def criar():
    cursor = conexao.cursor()

    email = request.form['email']
    nome = request.form['nome']
    curso = request.form['curso']

    if email and nome and curso != '':
        comando = f'INSERT INTO curso (email, nome, curso) VALUES ("{email}", "{nome}", "{curso}")'
        cursor.execute(comando)
        conexao.commit()



    return redirect('/')

    cursor.close()
    conexao.close()




@app.route('/atualizar', methods=['POST',])
def atualizar():

    email1 = request.form['email1']
    curso2 = request.form['curso2']

    update = f'UPDATE curso SET curso = "{curso2}" WHERE Email = "{email1}"'
    cursor.execute(update)
    conexao.commit()
    return redirect('/')

    cursor.close()
    conexao.close()




@app.route('/deletar', methods=['POST',])
def deletar():

    emaildelete = request.form['emaildelete']
    cursodelete = request.form['cursodelete']

    delete = f'DELETE from curso WHERE Email = "{emaildelete}" and Curso = "{cursodelete}"'
    cursor.execute(delete)
    conexao.commit()
    return redirect('/')

    cursor.close()
    conexao.close()


app.run(port=5000,host='localhost', debug = True )


