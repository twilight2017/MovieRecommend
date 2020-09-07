# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:02:48 2020

@author: hemo
"""

import sys
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')


from scipy import spatial
import pickle

def savefulldf():
    output = open('fulldf.pkl', 'wb')
    # Pickle dictionary using protocol 0.
    pickle.dump(fulldf, output)
    # Pickle the list using the highest protocol available.
    output.close()

def loadfulldf():
    pkl_file = open('fulldf.pkl', 'rb')
    fulldf = pickle.load(pkl_file)
    pkl_file.close()
    return fulldf

fulldf = loadfulldf()

columns =['original_title','genres','vote_average','genre_vec',
          'cast_vec','director','director_vec','words_vec','release_date','cast']
tmp = fulldf.copy()
tmp =tmp[columns]
tmp['id'] = list(range(0,fulldf.shape[0]))


def Similarity(movieId1, movieId2):
    # fulldf = pd.DataFrame(pd.read_csv('processed_data_fulldf.csv'))
    a = fulldf.iloc[movieId1]
    b = fulldf.iloc[movieId2]

    genresA = a['genre_vec']
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
        for x in range(16):
            neighbors.append(distances[x])
        return neighbors
    neighbors = getNeighbors(film)

    # for nei in neighbors:
      #  print( tmp.iloc[nei[0]][0]+" | Genres: "+
       #       str(tmp.iloc[nei[0]][1]).strip('[]').replace(' ','')+" | Rating: "
        #      +str(tmp.iloc[nei[0]][2])+" | Director: "+tmp.iloc[nei[0]][5]+
         #      " | Release_date: "+str(tmp.iloc[nei[0]][8])+" | Cast: "+str(tmp.iloc[nei[0]][9]).strip('[]').replace(' ',''))

    #print('\n')
    list1 = []
    for nei in neighbors:
        list1.append(tmp.iloc[nei[0]][0])
    print(list1)
    return list1

