__all__ = ["fnmatch", "fnmatchcase", "translate"]

def fnmatch(name: str, pat: str) -> bool: ...
def fnmatchcase(name: str, pat: str) -> bool: ...
def translate(pat: str) -> str: ...
