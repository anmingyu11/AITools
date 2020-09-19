import numpy as np


def chebyshev_inequality(series, k: float = 3, return_thresholds=False, reverse_result=False):
    """
    切比雪夫不等式，对任何分布形状的数据都适用。
    Return a boolean mask of outliers for a series
    using standard deviation, works column-wise.
    param nstd:
        Set number of standard deviations from the mean
        to consider an outlier
    :type k: ``float``
    param return_thresholds:
        True returns the lower and upper bounds, good for plotting.
        False returns the masked array
    :type return_thresholds: ``bool``
    """
    mu, sigma = np.mean(series), np.std(series)
    cut_off = sigma * k
    lower, upper = mu - cut_off, mu + cut_off
    res = [not reverse_result if x < lower or x > upper else reverse_result for x in series]
    if return_thresholds:
        return res, lower, upper
    else:
        return res


def out_iqr(s, k=1.5, return_thresholds=False):
    """
    Return a boolean mask of outliers for a series
    using interquartile range, works column-wise.
    param k:
        some cutoff to multiply by the iqr
    :type k: ``float``
    param return_thresholds:
        True returns the lower and upper bounds, good for plotting.
        False returns the masked array
    :type return_thresholds: ``bool``
    """
    # calculate interquartile range
    q25, q75 = np.percentile(s, 25), np.percentile(s, 75)
    iqr = q75 - q25
    # calculate the outlier cutoff
    cut_off = iqr * k
    lower, upper = q25 - cut_off, q75 + cut_off
    res = [True if x < lower or x > upper else False for x in s]
    if return_thresholds:
        return res, lower, upper
    else:  # identify outliers
        return res


def __test_chebyshev_inequality():
    ss = np.random.normal(loc=10, scale=10, size=10000)
    for k in range(1, 8, 1):
        mask = chebyshev_inequality(ss, k=k)
        ss_mask = ss[mask]
        print('-' * 70)
        print('k : {}'.format(k))
        print('before : {} after : {}'.format(len(ss), len(ss_mask)))
        print(ss_mask)
        print('-' * 70)
    pass


if __name__ == '__main__':
    __test_chebyshev_inequality()
    pass
