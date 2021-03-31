import itertools


def check_if_sorted(lst: list):
    return sorted(lst) == lst or sorted(lst, reverse=True) == lst


def union(set1, set2, final_type=list):
    return final_type(set(set1).union(set(set2)))


def intersection(set1, set2, final_type=list):
    return final_type(set(set1).intersection(set(set2)))


def difference(set1, set2, final_type=list):
    return final_type(set(set1).difference(set(set2)))


def is_subset_equal(set1, set2):
    set1 = set(set1)
    set2 = set(set2)
    return set1.issubset(set2) or set1 == set2


def pair_iter_list(ls):
    return list(zip(ls[:-1], ls[1:]))


def cartesian(x, y):
    return list(itertools.product(x, y))


# [1,2], [3,4]
# --> [1,3,2,4]
def chain_ziplist(x, y):
    return list(itertools.chain.from_iterable(list(zip(x, y))))
