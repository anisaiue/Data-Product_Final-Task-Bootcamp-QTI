from flask import Flask
from flask import Flask,render_template,url_for,request
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
	model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        data = [review]
        pred = model.predict(data)
        pred_prob = model.predict_proba(data)
    return render_template('result.html',prediction = pred, probability = pred_prob)