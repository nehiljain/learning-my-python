from ds.hash_map_base import HashMapBase


class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, i, k):
        """
        get the bucket at i
        if no bucket then riase keyerror
        get the key in the bucket
        """
        bucket = self._table[i]
        if bucket is None:
            raise KeyError(f'{k} doesnt exist')
        return bucket[k]
    
    def _bucket_setitem(self, i, k, v):
        """
        get bucket at i
        if no bucket, create a unsortedmap/dict at i
        set the k, v in the dict
        incr n if its not an update
        """
        bucket = self._table[i]
        if bucket is None:
            self._table[i] = {}
        orig_size = len(self._table[i])
        self._table[i][k] = v
        if len(self._table[i]) > orig_size:
            self._n += 1
        
    def _bucket_delitem(self, i, k):
        """
        get bucket at i
        if no nucket raise error
        del key in bucket
        decrease n
    """
        bucket = self._table[i]
        if bucket is None:
            raise KeyError(f'{k} doesnt exist')
        del bucket[k]
        self._n -= 1
 
    def __iter__(self):
        pass



