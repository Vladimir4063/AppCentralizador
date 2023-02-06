import time
from database.database_user import *
from database.database_replica10 import *
import csv
from urllib import request
from flask import Flask, render_template, request, redirect, url_for
from models.analyzer_models import string_to_integerList


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/dashboard')
def dashboard():
    print(id)

    f = open("csv/percentil95.csv")
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

    print(data)

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    labels2 = [row[0] for row in data]
    values2 = [row[1] for row in data]

    return render_template('admin/dashboard.html', 
        labels = labels, 
        values = values,
        labels2 = labels2,
        values2 = values2
    )

@app.route('/products/<objid>' , methods= ["GET", "POST"])
def products(objid):
    
    print(objid)
    return render_template('admin/products.html')

@app.route('/support')
def support():
    return render_template('admin/support.html')

@app.route('/integrations')
def integrations():
    return render_template('admin/integrations.html')

@app.route('/analyzer', methods=["GET", "POST"])
def analyzer():
    if request.method != 'POST':
        return render_template('admin/analyzer.html')

    # Validar ingresar datos
    objetivo = int(request.form['objetivo'])
    cant_pasos = int(request.form['cant_pasos'])
    pasos_ocultos = request.form['pasos_ocultos']
    fecha_hora = request.form['fecha_hora']

    pasos_ocultos = string_to_integerList(pasos_ocultos)

    print(type(objetivo))
    print(type(cant_pasos))
    print(type(pasos_ocultos))
    print(pasos_ocultos)
    print(fecha_hora)

    return render_template('admin/analyzer.html')

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        print(email)
        print(password)

        cursorUser = conexion_user.cursor()
        cursorUser.execute('''SELECT email FROM user WHERE email = ?''', (email,))
        print("EJECUTO")

        emaildb = cursorUser.fetchone()
        print(emaildb)

        #print(str(emaildb))
        # dateCursor = cursorUser.fetchall()
        # for row in dateCursor:
        #     print(row)

        if email == 'vgutierrez@atentus.com':
            if password == 'Pass.001':
                return redirect('/dashboard')
        else:
            return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
