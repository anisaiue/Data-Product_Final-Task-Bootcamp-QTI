from flask import Flask
from flask import Flask,render_template,url_for,request
import joblib

model_klasifikasi = open('model.pkl','rb')
model = joblib.load(model_klasifikasi)
app = Flask(__name__)

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
    return render_template('result.html',prediction = pred, probability1 = str(pred_prob[0,1]), probability2= str(pred_prob[0,0]))

if __name__ == '__main__':
	app.run(debug=True)