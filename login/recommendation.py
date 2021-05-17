
import matplotlib
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import numpy as np

animes = pd.read_csv('C:/Users/Sim/Desktop/animeweeb/bigrekosite/animeweeb/login/anime.csv', sep=',', encoding='latin-1', usecols=['title', 'genres'])
#spliting into array list or string list
animes['genres'] = animes['genres'].str.split('|') 
animes['genres'] = animes['genres'].fillna("").astype('str')

from sklearn.feature_extraction.text import TfidfVectorizer
#excluding stopwords like the,etc,and.
tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english') 
tfidf_matrix = tf.fit_transform(animes['genres'])
tfidf_matrix.shape

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cosine_sim[:4, :4]

#building 1-dimensional list with anime titles
titles = animes['title'].str.lower()
indices = pd.Series(animes.index, index=animes['title'].str.lower())

#peforming function to get anime recommendation 
#based on cosine similarity scores of anime titles
def genre_recommendations(title, out_count=10):
    try:
        title = title.lower()

        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[0], reverse=True)
        sim_scores = sim_scores[1:21]
        anime_indices = [i[0] for i in sim_scores]
        return list(titles.iloc[anime_indices].head(out_count))
    except:
        return list()

#print(genre_recommendations("one piece"))