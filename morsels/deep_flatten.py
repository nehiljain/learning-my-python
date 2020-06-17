from collections.abc import Iterable

def deep_flatten(inp):
  for item in inp:
    if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
      yield from deep_flatten(item)
    else:
      yield item
