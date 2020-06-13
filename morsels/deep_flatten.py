from collections.abc import Iterable
from itertools import chain

def deep_flatten(nested_list):
    output = nested_list
    need_flattening = True
    while need_flattening:
        output = list(chain.from_iterable(output))
        need_flattening = False            
        for item in output:
            if isinstance(item, Iterable):
                need_flattening = True

    return output

