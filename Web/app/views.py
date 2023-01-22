from app import app
from flask import render_template, request, url_for
from werkzeug import secure_filename
import os, shutil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn import svm
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
import pickle

def hitung(teks):
	try:
		#read model
		data = []
		data.append(teks)
		pkl_filename = "tmp/model_nn.pkl"
		with open(pkl_filename, 'rb') as file:  
		    model = pickle.load(file)
		Ypredict = model.predict(data)
		return str(Ypredict)
	except:
		return "Error"

	#return baru.iloc[1,:]

@app.route('/')
@app.route('/index')
def index():
	return render_template('home.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		lirik = str(request.form['lirik'])
		#return 'file uploaded successfully'
		hasil = hitung(lirik)
		return render_template('home.html',hasil = hasil)
