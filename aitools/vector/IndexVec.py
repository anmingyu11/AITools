def IndexFlatIP(vectors,k=50):
    d = vectors.shape[1]
    # the other index，需要以其他index作为基础
    index = faiss.IndexFlatIP(d)
    index.add(vectors)  # add may be a bit slower as well

    timer = Timer()
    display('searching started at : {}'.format(timer.get_now()))
    D, I = index.search(vectors[:300000], k)  # actual search
    display('faiss kmeans result : {} minutes'.format(timer.elapse_time()))

    display(D[:5])  # neighbors of the 5 first queries
    display(I[:5])

def IndexIVFFlat(vectors, nlist=100, nprobe=5, k=50):
    d = vectors.shape[1]
    # the other index，需要以其他index作为基础
    quantizer = faiss.IndexFlatIP(d)
    index = faiss.IndexIVFFlat(
        quantizer, d, nlist, faiss.METRIC_INNER_PRODUCT)

    # by default it performs inner-product search
    assert not index.is_trained
    index.train(vectors)
    assert index.is_trained
    index.nprobe = nprobe  # default nprobe is 1, try a few more
    index.add(vectors)  # add may be a bit slower as well

    timer = Timer()
    #display('searching started at : {}'.format(timer.get_now()))
    D, I = index.search(vectors[:300000], k)  # actual search
    #display('faiss kmeans result : {} minutes'.format(timer.elapse_time()))

    #display(D[:5])  # neighbors of the 5 first queries
    #display(I[:5])
    return D, I

def IndexIVFPQ(vectors, nlist=100,M=16, nprobe=200,k=50):
    d = vectors.shape[1]
    # the other index，需要以其他index作为基础
    index = faiss.index_factory(d, "IVF{},PQ{}".format(nlist, M), faiss.METRIC_INNER_PRODUCT)
    index.nprobe = nprobe

    # by default it performs inner-product search
    assert not index.is_trained
    index.train(vectors)
    assert index.is_trained
    index.nprobe = nprobe  # default nprobe is 1, try a few more
    index.add(vectors)  # add may be a bit slower as well
    timer = Timer()

    #display('searching started at : {}'.format(timer.get_now()))
    D, I = index.search(vectors[:100000], k)  # actual search
    #display('faiss kmeans result : {} minutes'.format(timer.elapse_time()))

    #display(D[:5])  # neighbors of the 5 first queries
    #display(I[:5])
    return D, I