import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score


def select_k_silhouette(X, max_n_cluster=10, show_plot=True, figsize=(12, 8)):
    '''
    This will take a long time when shape of X is large.
    :param X:
    :param max_n_cluster:
    :param show_plot:
    :param figsize:
    :return:
    '''
    max_n_cluster += 1
    res = []

    ks = range(2, max_n_cluster, 1)
    for k in ks:
        print('n_clusters : {}'.format(k))
        estimator = KMeans(n_clusters=k)
        estimator.fit(X)
        labels_ = estimator.labels_
        score = silhouette_score(X=X, labels=labels_)
        res.append(score)

    if not show_plot:
        return

    plt.figure(figsize=figsize)
    plt.xlabel('K')
    plt.ylabel('silhouette : k from {} to {}'.format(min(ks), max(ks)))
    plt.plot(ks, res, 'o-')
    plt.show()


def select_k_ch(X, max_n_cluster=10, show_plot=True, figsize=(12, 8)):
    max_n_cluster += 1
    res = []

    ks = range(2, max_n_cluster, 1)
    for k in ks:
        print('n_clusters : {}'.format(k))
        estimator = KMeans(n_clusters=k)
        estimator.fit(X)
        labels_ = estimator.labels_
        score = calinski_harabasz_score(X=X, labels=labels_)
        res.append(score)

    if not show_plot:
        return

    plt.figure(figsize=figsize)
    plt.xlabel('K')
    plt.ylabel('calinski_harabasz: k from {} to {}'.format(min(ks), max(ks)))
    plt.plot(ks, res, 'o-')
    plt.show()


def select_k_SSE(X, max_n_cluster=10, show_plot=True):
    max_n_cluster += 1
    res = []

    if len(X.shape) < 2:
        X = X.values.reshape(-1, 1)
    else:
        X = X.values
    ks = range(2, max_n_cluster, 1)
    for k in ks:
        print('n_clusters : {}'.format(k))
        estimator = KMeans(n_clusters=k)
        estimator.fit(X)
        labels_ = estimator.labels_
        score = estimator.inertia_
        res.append(score)

    if not show_plot:
        return

    if show_plot:
        plt.figure(figsize=(12, 6))
        plt.xlabel('K')
        plt.ylabel('SSE')
        plt.title('SSE: k from {} to {}'.format(min(ks), max(ks)))
        plt.plot(ks, res, 'o-')
        plt.show()

    return res, ks


def select_k_SSE_minibatch(X, max_n_cluster=10, show_plot=True):
    max_n_cluster += 1
    res = []

    if len(X.shape) < 2:
        X = X.values.reshape(-1, 1)
    else:
        X = X.values
    ks = range(2, max_n_cluster, 1)
    for k in ks:
        print('n_clusters : {}'.format(k))
        estimator = MiniBatchKMeans(n_clusters=k)
        estimator.fit(X)
        labels_ = estimator.labels_
        score = estimator.inertia_
        res.append(score)

    if not show_plot:
        return

    if show_plot:
        plt.figure(figsize=(12, 6))
        plt.xlabel('K')
        plt.ylabel('SSE')
        plt.title('SSE: k from {} to {}'.format(min(ks), max(ks)))
        plt.plot(ks, res, 'o-')
        plt.show()

    return res, ks
