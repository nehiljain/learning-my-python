from collections import UserDict

class PermaDict(UserDict):
    def __init__(self,  *args, silent=False, **kwargs):
        self.silent = silent
        super().__init__(*args, **kwargs)

    
    def __setitem__(self, key, value):
        if key not in self:
            return super().__setitem__(key, value)

        if not self.silent:
            raise KeyError(f"{key} already in dictionary")
        
    
    def force_set(self, key, value):
        return super().__setitem__(key, value)
    

    def update(self, *args, force=False, **kwargs ):
        if force:
            return self.data.update(*args, **kwargs)
        else:
            return super().update(*args, **kwargs)

