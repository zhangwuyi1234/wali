
import cPickle as p
import numpy as np
import chardet
def unpickle(file):
    import cPickle
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict
cc=unpickle("data_batch_0")
print(cc)
