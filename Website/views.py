from flask import Blueprint,render_template,request,jsonify
import numpy as np
import pickle
from flask_login import login_required ,current_user
from . import db
from .model import User,Post,Prediction
from datetime import datetime
views=Blueprint("views",__name__)
 
model=pickle.load(open('model.pkl','rb'))

@views.route('/home')
def home():
   return  render_template('home.html',user=current_user)

@views.route('/home',methods=['POST'])
def add_post():
    title=request.form.get('title')
    comment=request.form.get('comment')
    date_posted=datetime.now()
    new_post=Post(title=title,Comment=comment,date_posted=date_posted,user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()

    return  render_template('home.html',user=current_user)

@views.route('/business')
def business():
   return render_template('business.html',user=current_user)


@views.route('/add_companies')
def add_company():
   return render_template('AddCompany.html',user=current_user)


@views.route('/prediction',)
def salesprediction():
    return render_template('prediction.html',user=current_user)

@views.route('/prediction', methods=['POST'])
def predict():
    name=request.form.get('name')
    Store_Area=request.form.get('Store_Area')
    Items_Available=request.form.get('Items_Available')
    Customer_count=request.form.get('Customer_count')
    s=int(Store_Area)
    i=int(Items_Available)
    c=int(Customer_count)
    int_features = [s,i,c]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    date_created=datetime.now()
    new_post=Prediction(name=name,Store_Area=Store_Area,Items_Available=Items_Available,
    Customer_count=Customer_count,sale_prediction=output,date_created=date_created,user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()

    return render_template('prediction.html',user=current_user )

   


@views.route('/results', methods=['POST'])
def results():
    data = request.get_json(force=True)
    predict =model.predict([np.array(list(data.values()))])
    output = predict[0]
    return jsonify(output)

        