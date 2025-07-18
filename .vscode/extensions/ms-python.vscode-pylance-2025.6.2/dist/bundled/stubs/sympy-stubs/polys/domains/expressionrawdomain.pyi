from typing_extensions import Self

from sympy.core import Expr
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.series import Order
from sympy.utilities import public

@public
class ExpressionRawDomain(Field, CharacteristicZero, SimpleDomain):
    is_EXRAW = ...
    dtype = Expr
    zero = ...
    one = ...
    rep = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def __init__(self) -> None: ...
    @classmethod
    def new(cls, a): ...
    def to_sympy(self, a): ...
    def from_sympy(self, a) -> Expr: ...
    def convert_from(self, a, K): ...
    def get_field(self) -> Self: ...
    def sum(self, items) -> Order: ...

EXRAW = ...
