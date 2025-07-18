from io import TextIOWrapper
from typing import Any

split_path_re: Any
doctype_lookup_re: Any
tag_re: Any
xml_decl_re: Any

class ClassNotFound(ValueError): ...
class OptionError(Exception): ...

def get_choice_opt(options, optname, allowed, default=None, normcase: bool = False): ...
def get_bool_opt(options, optname, default=None): ...
def get_int_opt(options, optname, default=None): ...
def get_list_opt(options, optname, default=None): ...
def docstring_headline(obj): ...
def make_analysator(f): ...
def shebang_matches(text, regex): ...
def doctype_matches(text, regex): ...
def html_doctype_matches(text): ...
def looks_like_xml(text): ...
def surrogatepair(c): ...
def format_lines(var_name, seq, raw: bool = False, indent_level: int = 0): ...
def duplicates_removed(it, already_seen=()): ...

class Future:
    def get(self) -> None: ...

def guess_decode(text): ...
def guess_decode_from_terminal(text, term): ...
def terminal_encoding(term): ...

class UnclosingTextIOWrapper(TextIOWrapper):
    def close(self) -> None: ...
