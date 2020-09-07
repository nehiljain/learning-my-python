from collections import MutableMapping
from random import randrange


class HashMapBase(MutableMapping):
    def __init__(self, n = 101, p=109345121):
        self._table = n * [None]
        self._n = n
        self._p = p

        self._shift = 0 + randrange(p) # the b in [[ai + b] mod p] mod n
        self._scale = 1 + randrange(p-1) # the a in [[ai + b] mod p] mod n
        
    def _load_factor(self):
        return self._n / len(self._table)

    def _hash_function(self, k):
        """hashfunction builts with python hash and mad compression formula
        mad formula is 
            [(ai + b) mod p] mod n where
            a is scale
            b is shift
            p in prime number
            n is the length
        """
        return ((self._scale * hash(k) + self._shift) % self._p ) % self._n
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        real_i = self._hash_function(k)
        return self._bucket_getitem_(real_i, k)
    
    def __setitem__(self, k, v):
        real_i = self._hash_function(k)
        self._bucket_setitem(real_i, k)
        if self._load_factor() > 0.5:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        real_i = self._hash_function(k)
        return self._bucket_delitem___(real_i, k)

    def _resize(self, n):
        old = list(self.items()) # note we are using our hastable as a client here
        self._table = n * [None]
        self._n = 0
        for (k,v) in old:
            self[k] = v # we are using the hastable as a client, settings key and values