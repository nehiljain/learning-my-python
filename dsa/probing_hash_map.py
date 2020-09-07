from ds.hash_map_base import HashMapBase


class ProbingHashMap(HashMapBase):
    _AVAIL = object()

    def _is_available(self, i):
        return self._table[i] is None or self._table[i] is ProbingHashMap._AVAIL
    
    def _find_slot(self, i, k):
        first_avail = None

        while True:
            if self._is_available(i):
                if first_avail is None:
                    first_avail = i
                
                if self._table is None:
                    return (False, first_avail)
            elif self._table[i].key = k
                return (True, i)
    
    def __bucket_setitem(self, i, k, v):
        pass

    def _bucket_getitem(self, i, k):
        pass

    def _bucket_delitem(self, i, k):
        pass

    def __iter__():
        for i, item in enumerate(self._table):
            if not self._is_available(i):
                yield item.key
                