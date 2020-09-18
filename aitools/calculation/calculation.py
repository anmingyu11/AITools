import numpy as np

def inner_sub(l):
    if len(l) <= 1:
        raise Exception('len of l <=1 : {} '.format(len(l)))
    return np.array(l[1:]) - np.array(l[:-1])


def inner_sub_mean(l):
    if len(l) <= 1:
        raise Exception('len of l <=1 : {} '.format(len(l)))
    return np.mean(inner_sub(l))