import sys
from collections.abc import Generator
from typing import Any
from typing_extensions import TypeAlias

if sys.version_info >= (3, 10):
    from types import NotImplementedType
else:
    NotImplementedType: TypeAlias = Any
from typing import Literal, NoReturn

from sympy import Pow
from sympy.core.function import UndefinedFunction
from sympy.matrices.dense import MutableDenseMatrix
from sympy.series.order import Order

__all__ = ["diophantine", "classify_diop"]

class DiophantineSolutionSet(set):
    def __init__(self, symbols_seq, parameters) -> None: ...
    def add(self, solution) -> None: ...
    def update(self, *solutions) -> None: ...
    def dict_iterator(self) -> Generator[dict[Any, Any], Any, None]: ...
    def subs(self, *args, **kwargs) -> DiophantineSolutionSet: ...
    def __call__(self, *args) -> DiophantineSolutionSet: ...

class DiophantineEquationType:
    name: str = ...
    def __init__(self, equation, free_symbols=...) -> None: ...
    def matches(self) -> Literal[False]: ...
    @property
    def n_parameters(self) -> int: ...
    @property
    def parameters(self) -> Any: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...
    def pre_solve(self, parameters=...) -> None: ...

class Univariate(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class Linear(DiophantineEquationType):
    name = ...
    def matches(self) -> Any: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class BinaryQuadratic(DiophantineEquationType):
    name = ...
    def matches(self) -> Any | bool: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class InhomogeneousTernaryQuadratic(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...

class HomogeneousTernaryQuadraticNormal(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class HomogeneousTernaryQuadratic(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class InhomogeneousGeneralQuadratic(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...

class HomogeneousGeneralQuadratic(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...

class GeneralSumOfSquares(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class GeneralPythagorean(DiophantineEquationType):
    name = ...
    def matches(self) -> Literal[False]: ...
    @property
    def n_parameters(self) -> int: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

class CubicThue(DiophantineEquationType):
    name = ...
    def matches(self) -> Any | bool: ...

class GeneralSumOfEvenPowers(DiophantineEquationType):
    name = ...
    def matches(self) -> bool: ...
    def solve(self, parameters=..., limit=...) -> DiophantineSolutionSet: ...

all_diop_classes = ...
diop_known = ...

def diophantine(eq, param=..., syms=..., permute=...): ...
def merge_solution(var, var_t, solution) -> tuple[()] | tuple[Any, ...]: ...
def diop_solve(
    eq, param=...
) -> (
    tuple[None, ...]
    | set[Any]
    | tuple[None, None, None]
    | tuple[Any, Any, Any]
    | tuple[Any, ...]
    | tuple[Any | None, Any | None, Any | None]
    | set[tuple[int]]
    | None
): ...
def classify_diop(eq, _dict=...) -> tuple[Any, dict[Any, Any] | Any, Any]: ...
def diop_linear(eq, param=...) -> tuple[None, ...] | None: ...
def base_solution_linear(c, a, b, t=...) -> tuple[Any, Any] | tuple[Literal[0], Literal[0]] | tuple[None, None]: ...
def diop_univariate(eq) -> set[tuple[int]] | None: ...
def divisible(a, b) -> bool: ...
def diop_quadratic(eq, param=...) -> set[Any] | None: ...
def is_solution_quad(var, coeff, u, v) -> NotImplementedType | bool: ...
def diop_DN(D, N, t=...): ...
def cornacchia(a, b, m) -> set[Any] | None: ...
def PQa(P_0, Q_0, D) -> Generator[tuple[Any, Any, type[UndefinedFunction] | Any, Any, Any, Any], Any, NoReturn]: ...
def diop_bf_DN(
    D, N, t=...
) -> list[tuple[Literal[0], Literal[0]]] | list[tuple[Literal[0], Any]] | list[tuple[Any, Any]] | list[Any]: ...
def equivalent(u, v, r, s, D, N) -> bool: ...
def length(P, Q, D) -> int: ...
def transformation_to_DN(eq) -> tuple[Any, Any] | tuple[MutableDenseMatrix, MutableDenseMatrix] | None: ...
def find_DN(eq) -> tuple[Any, Any] | None: ...
def check_param(x, y, a, params) -> DiophantineSolutionSet | None: ...
def diop_ternary_quadratic(
    eq, parameterize=...
) -> tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | tuple[Any | None, Any | None, Any | None] | None: ...
def transformation_to_normal(eq) -> MutableDenseMatrix | None: ...
def parametrize_ternary_quadratic(eq) -> tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | None: ...
def diop_ternary_quadratic_normal(
    eq, parameterize=...
) -> tuple[None, None, None] | tuple[Any, Any, Any] | tuple[Any, ...] | tuple[Any | None, Any | None, Any | None] | None: ...
def sqf_normal(
    a, b, c, steps=...
) -> tuple[tuple[Any | Order, ...], tuple[Any, ...], tuple[Any, Any, Any]] | tuple[Any, Any, Any]: ...
def square_factor(a) -> Order: ...
def reconstruct(A, B, z): ...
def ldescent(
    A, B
) -> (
    tuple[Any, Any, Any]
    | tuple[Literal[1], Literal[1], Literal[0]]
    | tuple[Literal[1], Literal[0], Literal[1]]
    | tuple[Any, ...]
    | None
): ...
def descent(
    A, B
) -> (
    tuple[Any, Any, Any]
    | tuple[Literal[1], Literal[0], Literal[1]]
    | tuple[Literal[1], Literal[1], Literal[0]]
    | tuple[Literal[0], Literal[1], Literal[1]]
    | tuple[Any, ...]
): ...
def gaussian_reduce(w, a, b) -> tuple[Any, Any | int]: ...
def dot(u, v, w, a, b): ...
def norm(u, w, a, b) -> Pow: ...
def holzer(x, y, z, a, b, c) -> tuple[int, ...]: ...
def diop_general_pythagorean(eq, param=...) -> None: ...
def diop_general_sum_of_squares(eq, limit=...) -> set[Any] | None: ...
def diop_general_sum_of_even_powers(eq, limit=...) -> set[Any] | None: ...
def partition(n, k=..., zeros=...) -> Generator[tuple[Any, ...] | Any, Any, None]: ...
def prime_as_sum_of_two_squares(p) -> tuple[int, int] | None: ...
def sum_of_three_squares(
    n,
) -> tuple[Literal[0], Literal[0], Literal[0]] | tuple[Any, ...] | tuple[Any, Literal[0], Literal[0]] | None: ...
def sum_of_four_squares(n) -> tuple[Literal[0], Literal[0], Literal[0], Literal[0]] | tuple[Any, ...]: ...
def power_representation(
    n, p, k, zeros=...
) -> Generator[tuple[Any, ...] | tuple[Literal[0], ...] | tuple[int] | tuple[Any] | tuple[int, int] | None, Any, None]: ...

sum_of_powers = ...

def pow_rep_recursive(n_i, k, n_remaining, terms, p) -> Generator[tuple[Any, ...] | Any, Any, None]: ...
def sum_of_squares(
    n, k, zeros=...
) -> Generator[tuple[Any, ...] | tuple[Literal[0], ...] | tuple[int] | tuple[Any] | tuple[int, int] | None, Any, None]: ...
