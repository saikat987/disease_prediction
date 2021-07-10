import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pickle_model.pkl', 'rb'))
l=['receiving_blood_transfusion', 'red_sore_around_nose',
       'abnormal_menstruation', 'continuous_sneezing', 'breathlessness',
       'blackheads', 'shivering', 'dizziness', 'back_pain', 'unsteadiness',
       'yellow_crust_ooze', 'muscle_weakness', 'loss_of_balance', 'chills',
       'ulcers_on_tongue', 'stomach_bleeding', 'lack_of_concentration', 'coma',
       'neck_pain', 'weakness_of_one_body_side', 'diarrhoea',
       'receiving_unsterile_injections', 'headache', 'weight_loss',
       'fast_heart_rate', 'pain_behind_the_eyes', 'sweating', 'mucoid_sputum',
       'spotting_ urination', 'sunken_eyes', 'dischromic _patches', 'nausea',
       'dehydration', 'loss_of_appetite', 'abdominal_pain', 'stomach_pain',
       'yellowish_skin', 'altered_sensorium', 'chest_pain', 'muscle_wasting',
       'vomiting', 'mild_fever', 'high_fever', 'red_spots_over_body',
       'dark_urine', 'itching', 'yellowing_of_eyes', 'fatigue', 'joint_pain',
       'muscle_pain']
dict_to_list={}
for i,j in enumerate(l):
    dict_to_list[j]=i


@app.route('/')
def home():
    return render_template('index1.html')


@app.route('/showinput',methods=['POST'])
def showinput():
    '''
    For rendering results on HTML GUI
    '''
    hello = request.form.getlist('all')
    print(hello)
    input_from_user=[0]*len(l)
    for i in hello:
        input_from_user[dict_to_list[i]]=1

    if len(hello)<3:
        return render_template('index1.html', prediction_text='Choose atleast 3 symptoms')

    prediction = model.predict([input_from_user])

    #output = round(prediction[0], 2)

    return render_template('index1.html', prediction_text='Predicted disease is {}'.format(prediction[0]))
