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

data = pd.read_csv("final_data_lagu_dan_emosi.csv")
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()
data['Lirik_bersih'] = data['Lirik'].apply(lambda x: stopword.remove(x))
#Train data
X_train = data['Lirik_bersih'][:800] #count_vect.fit_transform()
y_train = data['Emotion'][:800]
#test data
X_test = data['Lirik_bersih'][801:1060]
y_test = data['Emotion'][801:1060]
#SGD
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                           alpha=1e-3, random_state=42))])
text_clf.fit(X_train, y_train)  
predicted = text_clf.predict(X_test)
print("Akurasi: "+ str(np.mean(predicted == y_test)))
#Classification Report
print(metrics.classification_report(y_test, predicted, target_names=['Joy','Sad']))

#Neural Networks
text_clf_nn = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1))])
text_clf_nn.fit(X_train, y_train)  
predicted = text_clf_nn.predict(X_test)
print("Akurasi: "+ str(np.mean(predicted == y_test)))
print(metrics.classification_report(y_test, predicted, target_names=['Joy','Sad']))

#Decision Tree
text_clf_dt = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', tree.DecisionTreeClassifier())])
text_clf_dt.fit(X_train, y_train)  
predicted = text_clf_dt.predict(X_test)
print("Akurasi: "+ str(np.mean(predicted == y_test)))
print(metrics.classification_report(y_test, predicted, target_names=['Joy','Sad']))