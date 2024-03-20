from typing import Any, Optional, overload, Typing, Sequence, Iterable, Union, Callable
from enum import Enum
import nanobind_example

class Foo:
    """
    None
    """

    def __init__(self) -> None:
        ...
    
    @property
    def name(self) -> str:
        ...
    @name.setter
    def name(self, arg: str, /) -> None:
        ...
    
    def print(self) -> None:
        ...
    
class GeekyOdyssey:
    """
    None
    """

    def __init__(self) -> None:
        ...
    
    def call_callable(self, arg: str, /) -> None:
        ...
    
    @property
    def callable(self) -> Callable[[str], None]:
        ...
    @callable.setter
    def callable(self, arg: Callable[[str], None], /) -> None:
        ...
    
    def get_shared_foo(self) -> nanobind_example.nanobind_example_ext.Foo:
        ...
    
    def get_vector(self) -> list[int]:
        ...
    
    instances: int
    
    def loop(self, count: int) -> None:
        ...
    
    @property
    def name(self) -> int:
        ...
    @name.setter
    def name(self, arg: int, /) -> None:
        ...
    
    def print(self) -> str:
        ...
    
    def print_vector(self, numbers: list[int]) -> None:
        ...
    
    def set_callable(self, callable: Callable[[str], None]) -> None:
        ...
    
    def sprint() -> str:
        ...
    
def add(a: int, b: int) -> int:
    ...

def mul(a: int, b: int) -> int:
    ...

def mul2(a1: int, b: int) -> int:
    ...

def mul3(a: int, b: int) -> int:
    ...

