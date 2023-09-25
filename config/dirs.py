global _cache
_cache = {}

from pathlib import Path

def temp () -> Path:
    global _cache
    _temp = _cache.get('temp',None)
    if _temp :
        return Path(_temp)
    import tempfile
    _cache ['temp'] = tempfile.mktemp()
    return temp()