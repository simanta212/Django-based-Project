import pandas as pd
import numpy as np
import joblib
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
df = pd.read_csv('IMDB_Dataset.csv', sep=',')

df.sentiment.value_counts()
df['sentiment_num'] = df.sentiment.map({'positive':1,'negative':0})
stopset = set(stopwords.words('english'))
vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stopset)
y = df.sentiment_num
X= vectorizer.fit_transform(df.review)

#lets train and split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42)

##lets train a naive bayes classifier
clf = naive_bayes.MultinomialNB()
clf.fit(X_train, y_train)

#lets check model accuracy
print('Accuracy is', clf.score(X_test,y_test)*100,'%')
unprocessed_feature = input("Enter a comment : ")
movie_reviews_array=np.array([unprocessed_feature])
movie_review_vector = vectorizer.transform(movie_reviews_array)
predictor = clf.predict(movie_review_vector)
if (predictor==1):
    print ("positive Comment")
else:
    print("negative")

#save the model to the disk
#filename = 'final_model.sav'
#oblib.dump(clf, filename)

