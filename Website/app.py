import numpy as np
from flask import Flask,request,jsonify,render_template,flash
import pickle


app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
@app.route('/login')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email=request.form.get('email')
    password=request.form.get('email')
    return render_template('home.html')

@app.route('/company')
def company():
    return render_template('addcompany.html')

@app.route('/register')
def register():
   
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def userRegistration():
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    id=request.form.get('id')
    gendar=request.form.get('gendar')
    email=request.form.get('email')
    password1=request.form.get('password1')
    password2=request.form.get('password2')

    if len(email<4):
        flash("invalid email",category="error")
    elif len(firstname<2):
        flash("must not be empty",category="error")
    elif password1 != password2:
        flash("password does not match",category="error")
    else:
        #add user to databasa
        flash("invalid email",category="error")
        pass
    return render_template('login.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/prediction')
def salesprediction():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

@app.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    predict =model.predict([np.array(list(data.values()))])
    output = predict[0]
    return jsonify(output)

