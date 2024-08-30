from flask import Flask, render_template, request, flash, redirect,session
from flask_session import Session


import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import mysql.connector
import random
import json 
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
def connect():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pfe"
    )
    mycursor = mydb.cursor()
    return mydb,mycursor
def logindb(username,password):
    mydb,cursor=connect()
    cursor.execute("SELECT * FROM user WHERE username =%s AND password  =%s",(username,password))
    users = cursor.fetchall()
    if users:
        print('Login OK.')
        return "done"
    else:
        print('Login not ok .')
        return "not done"

def signup(name,username,password,phone):
    user=(name,username,password,phone)
    mydb,cursor=connect()
    sql = "INSERT INTO user (name, username,password,phone) VALUES (%s, %s,%s,%s)"    
    cursor.execute(sql, user)    
    mydb.commit()

def predict(values, dic):
    if len(values) == 8:
        model = pickle.load(open('models/diabet_disease.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('models/Breast_Cancer_predicting_model1.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('models/kidney_model1.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('models/liver.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        mydb,cursor=connect()
        # record the user name
        username=request.form.get("username")
        password=request.form.get("pswd")
        msg=logindb(username,password)
        if (msg=="done"):
            session["username"] = username
            return render_template('index.html')

        #print(msg)
        # redirect to the main page
        
    return render_template('login.html')
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        mydb,cursor=connect()
        # record the user name
        name=request.form.get("name")
        username=request.form.get("username")
        phone=request.form.get("phone")
        password=request.form.get("pswd")
        signup(name,username,phone,password)
        session["username"] = username
        return render_template('index.html')
    return render_template('register.html')
@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")

@app.route("/formulaire", methods=['GET', 'POST'])
def form():
    return render_template('formulaire.html')    
@app.route("/diabetes", methods=['GET', 'POST'])
def diabetesPage():
    return render_template('diabetes.html')
@app.route("/indexDiabete")
def indexDiabete():
    return render_template('indexDiabete.html')

@app.route("/indexbreastcancer")
def indexbreastcancer():
    return render_template('indexbreastcancer.html')

@app.route("/indexBreastimage")
def indexBreastimage():
    return render_template('indexBreastimage.html')
@app.route("/IndexTumeur")
def IndexTumeur():
    return render_template('IndexTumeur.html')
@app.route("/indexDerma")
def indexDerma():
    return render_template('indexDerma.html')
@app.route("/indexHeart")
def indexHeart():
    return render_template('indexHeart.html')

@app.route("/indexFormulaire")
def indexFormulaire():
    return render_template('indexFormulaire.html')
@app.route("/indexLiver")
def indexLiver():
    return render_template('indexLiver.html')
@app.route("/indexPneumonia")
def indexPneumonie():
    return render_template('indexPneumonia.html')
@app.route("/indexMalaria")
def indexMalaria():
    return render_template('indexMalaria.html')


@app.route("/cancer", methods=['GET', 'POST'])
def cancerPage():
    return render_template('breast_cancer.html')


@app.route("/heart", methods=['GET', 'POST'])
def heartPage():
    return render_template('heart.html')


@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')

@app.route("/liver", methods=['GET', 'POST'])
def liverPage():
    return render_template('liver.html')

@app.route("/malaria", methods=['GET', 'POST'])
def malariaPage():
    return render_template('malaria.html')
@app.route("/tumeur", methods=['GET', 'POST'])
def tumerPage():
    return render_template('tumeur.html')
@app.route("/breast_cancer_image", methods=['GET', 'POST'])
def cancerimagePage():
    return render_template('breat_cancer_image.html')
@app.route("/derma", methods=['GET', 'POST'])
def dermaPage():
    return render_template('derma.html')

@app.route("/pneumonia", methods=['GET', 'POST'])
def pneumoniaPage():
    return render_template('pneumonia.html')

@app.route("/malariapredict", methods = ['POST', 'GET'])
def malariapredictPage():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image'])
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,3))
                img = img.astype(np.float64)
                model = load_model("models/malaria1 (1).h5")
                pred = np.argmax(model.predict(img)[0])
        except:
            message = "Veuillez Inserer L'Image"
            return render_template('malaria.html', message = message)
    return render_template('malaria_predict.html', pred = pred)

@app.route("/pneumoniapredict", methods = ['POST', 'GET'])
def pneumoniapredictPage():
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,1))
                img = img / 255.0
                model = load_model("models/pneumonia.h5")
                pred = np.argmax(model.predict(img)[0])
        except:
            message = "Veuillez Inserer L'Image"
            return render_template('pneumonia.html', message = message)
    return render_template('pneumonia_predict.html', pred = pred)




@app.route("/breast_cancer_imagepredict", methods = ['POST', 'GET'])
def breastcancerimagepredictPage():
    pred=0
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                f = request.files['image']
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((64,64))
                img = np.asarray(img)
                img = img.reshape((139,64,64,3))
                img = img / 255.0
                model = load_model("models/cancer_cnn (1).h5")

                img = image.load_img(f.filename, target_size = (50,50))
                img = image.img_to_array(img)
                img = np.expand_dims(img, axis = 0)
                preds = model.predict(img)
                #training_set.class_indices
                

                pred = preds[0][0] 
        except Exception as e:
            print(e)
            pred=0
            message = "Veuillez Inserer L'Image"
            return render_template('breat_cancer_image.html', message = message)
    return render_template('breast_image_predict.html' , pred = pred )



@app.route("/tumorpredict", methods = ['POST', 'GET'])
def tumorpredictPage():
    pred=0
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                f = request.files['image']
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((64,64))
                img = np.asarray(img)
                img = img.reshape((139,64,64,3))
                img = img / 255.0
                model = load_model("models/trrrrr.h5")

                img = image.load_img(f.filename, target_size = (64, 64))
                img = image.img_to_array(img)
                img = np.expand_dims(img, axis = 0)
                preds = model.predict(img)
                #training_set.class_indices
                

                pred = preds[0][0] 
        except Exception as e:
            print(e)
            pred=0
            message = "Veuillez Inserer L'Image"
            return render_template('tumeur.html', message = message)
    return render_template('tumeur_predict.html' , pred = pred )


@app.route("/dermapredict", methods = ['POST', 'GET'])
def dermapredictPage():
    pred=0
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                f = request.files['image']
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((64,64))
                img = np.asarray(img)
                img = img.reshape((139,64,64,3))
                img = img / 255.0
                model = load_model("models/derma (1).h5")

                img = image.load_img(f.filename, target_size = (224, 224))
                img = image.img_to_array(img)
                img = np.expand_dims(img, axis = 0)
                preds = model.predict(img)
                #training_set.class_indices
                

                pred = preds[0][0] 
        except Exception as e:
            print(e)
            pred=0
            message = "Veuillez Inserer L'Image"
            return render_template('derma.html', message = message)
    return render_template('derma_predict.html' , pred = pred )



@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except Exception as ex:
        print(ex)
        message = "Veuillez Inserer Les Données valides"
        return render_template("index.html", message = message)

    if (pred==1):    
        return render_template('sicklyPerson.html', pred = pred)
    else :
        return render_template('healthyPerson.html', pred = pred)


if __name__ == '__main__':

    app.run(host="0.0.0.0",port="5000")