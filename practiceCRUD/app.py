import sys
from warnings import catch_warnings
from flask import Flask,request, url_for, redirect, render_template
import mysql.connector

app = Flask(__name__)


midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jojaseir29",
    database="prueba"
)

cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/post/<post_id>' , methods=['GET','POST'])
def getpost(post_id):
    if request.method == 'GET':
        return 'Post ' + post_id
    else:
        return 'debe utilizar el methodo get'

 
@app.route('/form' , methods=['GET', 'POST'])
def getform():
#    return redirect(url_for('getpost', post_id= 2))
    # print (url_for('getpost', post_id = 2))
    # print (request.form)
    # print (request.form['llave1'])
    # return 'lele'
    return render_template('page.html')

# @app.route('/data' , methods=['GET'])
# def getdata():
#     return {
#         "username":"Jose Arosemena",
#         "email":"j@gmail.com"
#     }

@app.route('/data' , methods=['GET'])
def getdata():
    cursor.execute('select * from usuarios')
    usuarios = cursor.fetchall()
    return render_template('page.html', usuarios=usuarios)

@app.route('/home' , methods=['GET'])
def home():
    return render_template('home.html', mensaje='hola mundo por parametro en la pagina')

@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        password= request.form['password']
        password2 = request.form['password2']
        try:
      
            sql = "INSERT INTO Usuarios (username,email,edad) VALUES (%s,%s,%s)"
            values = (username,email,int(edad))
            cursor.execute(sql,values)
            midb.commit()

        except:
            print("some error in sql statement",sys.exc_info())
        finally:
            return redirect(url_for('getdata'))

    return render_template('crear.html')


