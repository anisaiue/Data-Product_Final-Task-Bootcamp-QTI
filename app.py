from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from sklearn.model_selection import train_test_split

app = Flask(__name__)
api = Api(app)

with open('model.pkl', 'rb') as f:
	model = pickle.load(f)

with open('cleaning.pkl', 'rb') as f:
	clean = pickle.load(f)

@app.route('/predict',methods=['POST'])
def predict():
    df = pd.read_csv("review_crawling.csv")
    #Featuring label
    df['label'] = df['rate'].map({1:0,2:0,3:0,4:1,5:1})
    #Cleansing data
    reviews = []
    for index, row in df.iterrows():
        reviews.append(clean(row['review']))
    df['review']=reviews

    #Stopword remover
    factory = StopWordRemoverFactory()
    stopwords = factory.create_stop_word_remover()
    reviews = []
    for index, row in df.iterrows():
        reviews.append(stopwords.remove(row['review']))
    df['review']=reviews

    #Split data train test
    sentences = df['reviews'].values
    y = df['reviews'].values
    x_train, x_test, y_train, y_test = train_test_split(sentences, y, test_size=0.2, random_state=1000)

    #build model
    model.fit(x_train, y_train)
    model.score(x_test, y_test)
