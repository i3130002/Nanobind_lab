from typing import Any, Optional, overload, Typing, Sequence, Iterable, Union, Callable
from enum import Enum
import nanobind_example.nanobind_example_ext

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
    
    def get_shared_foo(self) -> nanobind_example.nanobind_example_ext.Foo:
        ...
    
    def get_vector(self) -> list[int]:
        ...
    
    instances: int
    
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

