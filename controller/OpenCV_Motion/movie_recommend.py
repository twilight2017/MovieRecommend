#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('ggplot')
import json
import warnings
warnings.filterwarnings('ignore')#忽略警告


from scipy import spatial
# fulldf = pd.read_csv("fulldf.csv")
# fulldf['cast_vec'] = fulldf['cast'].apply(lambda x:binary(x))
# fulldf['genre_vec'] = fulldf['genres'].apply(lambda x: binary(x))
# fulldf['director_vec'] = fulldf['director'].apply(lambda x:binary(x))
# fulldf['words_vec'] = fulldf['keywords'].apply(lambda x: binary(x))
tmp = pd.read_csv('tmp.csv')


# columns =['original_title','genres','vote_average','genre_vec','cast_vec','director','director_vec','words_vec']
# tmp = fulldf.copy()
# tmp =tmp[columns]
# tmp['id'] = list(range(0,fulldf.shape[0]))


def Similarity(movieId1, movieId2):
    # fulldf = pd.DataFrame(pd.read_csv('processed_data_fulldf.csv'))
    # a = fulldf.iloc[movieId1]
    # b = fulldf.iloc[movieId2]

    a = tmp.iloc[movieId1]
    b = tmp.iloc[movieId2]

    genresA = a['genre_vec']
    print(genresA, type(genresA))
    genresB = b['genre_vec']
    genreDistance = spatial.distance.cosine(genresA, genresB)

    castA = a['cast_vec']
    castB = b['cast_vec']
    castDistance = spatial.distance.cosine(castA, castB)

    directA = a['director_vec']
    directB = b['director_vec']
    directDistance = spatial.distance.cosine(directA, directB)

    wordsA = a['words_vec']
    wordsB = b['words_vec']
    wordsDistance = spatial.distance.cosine(wordsA, wordsB)
    return genreDistance + directDistance + castDistance + wordsDistance


import operator
def recommend(name):
    # tmp = pd.DataFrame(pd.read_csv('processed_data.csv'))

    film=tmp[tmp['original_title'].str.contains(name)].iloc[0].to_frame().T
    print('Selected Movie: ',film.original_title.values[0])
    def getNeighbors(baseMovie):
        distances = []
        for index, movie in tmp.iterrows():
            if movie['id'] != baseMovie['id'].values[0]:
                dist = Similarity(baseMovie['id'].values[0], movie['id'])
                distances.append((movie['id'], dist))

        distances.sort(key=operator.itemgetter(1))

        neighbors = []
        for x in range(10):
            neighbors.append(distances[x])
        return neighbors
    neighbors = getNeighbors(film)
    print('\nRecommended Movies: \n')

    for nei in neighbors:
        print( tmp.iloc[nei[0]][0]+" | Genres: "+
              str(tmp.iloc[nei[0]][1]).strip('[]').replace(' ','')+" | Rating: "
              +str(tmp.iloc[nei[0]][2]))

    print('\n')



