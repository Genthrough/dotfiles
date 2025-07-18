import sys
from collections.abc import Iterable, Iterator
from typing import Any, Final, Generic, Literal, TypeVar, overload
from typing_extensions import Self, TypeAlias

# Undocumented length constants
IPV4LENGTH: Final = 32
IPV6LENGTH: Final = 128

_A = TypeVar("_A", IPv4Address, IPv6Address)
_N = TypeVar("_N", IPv4Network, IPv6Network)

_RawIPAddress: TypeAlias = int | str | bytes | IPv4Address | IPv6Address
_RawNetworkPart: TypeAlias = IPv4Network | IPv6Network | IPv4Interface | IPv6Interface

def ip_address(address: _RawIPAddress) -> IPv4Address | IPv6Address: ...
def ip_network(
    address: _RawIPAddress | _RawNetworkPart | tuple[_RawIPAddress] | tuple[_RawIPAddress, int], strict: bool = True
) -> IPv4Network | IPv6Network: ...
def ip_interface(
    address: _RawIPAddress | _RawNetworkPart | tuple[_RawIPAddress] | tuple[_RawIPAddress, int],
) -> IPv4Interface | IPv6Interface: ...

class _IPAddressBase:
    @property
    def compressed(self) -> str: ...
    @property
    def exploded(self) -> str: ...
    @property
    def reverse_pointer(self) -> str: ...
    if sys.version_info < (3, 14):
        @property
        def version(self) -> int: ...

class _BaseAddress(_IPAddressBase):
    def __add__(self, other: int) -> Self: ...
    def __hash__(self) -> int: ...
    def __int__(self) -> int: ...
    def __sub__(self, other: int) -> Self: ...
    def __format__(self, fmt: str) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: Self) -> bool: ...
    if sys.version_info >= (3, 11):
        def __ge__(self, other: Self) -> bool: ...
        def __gt__(self, other: Self) -> bool: ...
        def __le__(self, other: Self) -> bool: ...
    else:
        def __ge__(self, other: Self, NotImplemented: Any = ...) -> bool: ...
        def __gt__(self, other: Self, NotImplemented: Any = ...) -> bool: ...
        def __le__(self, other: Self, NotImplemented: Any = ...) -> bool: ...

class _BaseNetwork(_IPAddressBase, Generic[_A]):
    network_address: _A
    netmask: _A
    def __contains__(self, other: Any) -> bool: ...
    def __getitem__(self, n: int) -> _A: ...
    def __iter__(self) -> Iterator[_A]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: Self) -> bool: ...
    if sys.version_info >= (3, 11):
        def __ge__(self, other: Self) -> bool: ...
        def __gt__(self, other: Self) -> bool: ...
        def __le__(self, other: Self) -> bool: ...
    else:
        def __ge__(self, other: Self, NotImplemented: Any = ...) -> bool: ...
        def __gt__(self, other: Self, NotImplemented: Any = ...) -> bool: ...
        def __le__(self, other: Self, NotImplemented: Any = ...) -> bool: ...

    def address_exclude(self, other: Self) -> Iterator[Self]: ...
    @property
    def broadcast_address(self) -> _A: ...
    def compare_networks(self, other: Self) -> int: ...
    def hosts(self) -> Iterator[_A]: ...
    @property
    def is_global(self) -> bool: ...
    @property
    def is_link_local(self) -> bool: ...
    @property
    def is_loopback(self) -> bool: ...
    @property
    def is_multicast(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_reserved(self) -> bool: ...
    @property
    def is_unspecified(self) -> bool: ...
    @property
    def num_addresses(self) -> int: ...
    def overlaps(self, other: _BaseNetwork[IPv4Address] | _BaseNetwork[IPv6Address]) -> bool: ...
    @property
    def prefixlen(self) -> int: ...
    def subnet_of(self, other: Self) -> bool: ...
    def supernet_of(self, other: Self) -> bool: ...
    def subnets(self, prefixlen_diff: int = 1, new_prefix: int | None = None) -> Iterator[Self]: ...
    def supernet(self, prefixlen_diff: int = 1, new_prefix: int | None = None) -> Self: ...
    @property
    def with_hostmask(self) -> str: ...
    @property
    def with_netmask(self) -> str: ...
    @property
    def with_prefixlen(self) -> str: ...
    @property
    def hostmask(self) -> _A: ...

class _BaseV4:
    if sys.version_info >= (3, 14):
        version: Final = 4
        max_prefixlen: Final = 32
    else:
        @property
        def version(self) -> Literal[4]: ...
        @property
        def max_prefixlen(self) -> Literal[32]: ...

class IPv4Address(_BaseV4, _BaseAddress):
    def __init__(self, address: object) -> None: ...
    @property
    def is_global(self) -> bool: ...
    @property
    def is_link_local(self) -> bool: ...
    @property
    def is_loopback(self) -> bool: ...
    @property
    def is_multicast(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_reserved(self) -> bool: ...
    @property
    def is_unspecified(self) -> bool: ...
    @property
    def packed(self) -> bytes: ...
    if sys.version_info >= (3, 13):
        @property
        def ipv6_mapped(self) -> IPv6Address: ...

class IPv4Network(_BaseV4, _BaseNetwork[IPv4Address]):
    def __init__(self, address: object, strict: bool = ...) -> None: ...

class IPv4Interface(IPv4Address):
    netmask: IPv4Address
    network: IPv4Network
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def hostmask(self) -> IPv4Address: ...
    @property
    def ip(self) -> IPv4Address: ...
    @property
    def with_hostmask(self) -> str: ...
    @property
    def with_netmask(self) -> str: ...
    @property
    def with_prefixlen(self) -> str: ...

class _BaseV6:
    if sys.version_info >= (3, 14):
        version: Final = 6
        max_prefixlen: Final = 128
    else:
        @property
        def version(self) -> Literal[6]: ...
        @property
        def max_prefixlen(self) -> Literal[128]: ...

class IPv6Address(_BaseV6, _BaseAddress):
    def __init__(self, address: object) -> None: ...
    @property
    def is_global(self) -> bool: ...
    @property
    def is_link_local(self) -> bool: ...
    @property
    def is_loopback(self) -> bool: ...
    @property
    def is_multicast(self) -> bool: ...
    @property
    def is_private(self) -> bool: ...
    @property
    def is_reserved(self) -> bool: ...
    @property
    def is_unspecified(self) -> bool: ...
    @property
    def packed(self) -> bytes: ...
    @property
    def ipv4_mapped(self) -> IPv4Address | None: ...
    @property
    def is_site_local(self) -> bool: ...
    @property
    def sixtofour(self) -> IPv4Address | None: ...
    @property
    def teredo(self) -> tuple[IPv4Address, IPv4Address] | None: ...
    @property
    def scope_id(self) -> str | None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...

class IPv6Network(_BaseV6, _BaseNetwork[IPv6Address]):
    def __init__(self, address: object, strict: bool = ...) -> None: ...
    @property
    def is_site_local(self) -> bool: ...

class IPv6Interface(IPv6Address):
    netmask: IPv6Address
    network: IPv6Network
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def hostmask(self) -> IPv6Address: ...
    @property
    def ip(self) -> IPv6Address: ...
    @property
    def with_hostmask(self) -> str: ...
    @property
    def with_netmask(self) -> str: ...
    @property
    def with_prefixlen(self) -> str: ...

def v4_int_to_packed(address: int) -> bytes: ...
def v6_int_to_packed(address: int) -> bytes: ...

# Third overload is technically incorrect, but convenient when first and last are return values of ip_address()
@overload
def summarize_address_range(first: IPv4Address, last: IPv4Address) -> Iterator[IPv4Network]: ...
@overload
def summarize_address_range(first: IPv6Address, last: IPv6Address) -> Iterator[IPv6Network]: ...
@overload
def summarize_address_range(
    first: IPv4Address | IPv6Address, last: IPv4Address | IPv6Address
) -> Iterator[IPv4Network] | Iterator[IPv6Network]: ...
def collapse_addresses(addresses: Iterable[_N]) -> Iterator[_N]: ...
@overload
def get_mixed_type_key(obj: _A) -> tuple[int, _A]: ...
@overload
def get_mixed_type_key(obj: IPv4Network) -> tuple[int, IPv4Address, IPv4Address]: ...
@overload
def get_mixed_type_key(obj: IPv6Network) -> tuple[int, IPv6Address, IPv6Address]: ...

class AddressValueError(ValueError): ...
class NetmaskValueError(ValueError): ...
