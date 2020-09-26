import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import cosine

def inner_sub(l):
    if len(l) <= 1:
        raise Exception('len of l <=1 : {} '.format(len(l)))
    return np.array(l[1:]) - np.array(l[:-1])


def inner_sub_mean(l):
    if len(l) <= 1:
        raise Exception('len of l <=1 : {} '.format(len(l)))
    return np.mean(inner_sub(l))

def euclid_distance1(p1 , p2):
    return np.linalg.norm(p1-p2)

def euclid_distance2(p1 , p2):
    return np.sqrt(np.sum(np.square(vec1 - vec2)))

def cosine1(v1 , v2):
    return cosine(v1,v2)

def cosine2(v1 , v2):
    return 1 - cosine_similarity(v1.reshape(1,-1),v2.reshape(1,-1))