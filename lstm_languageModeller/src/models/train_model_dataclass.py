"""Exploring data classes in depth"""
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Maybe to generate id?"""
    return "".join(random.choices(string.ascii_uppercase, k=11))


@dataclass()
class Person:
    """ Generating person attributes"""
    name: str
    age: int
    salary: float
    actived: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id_gen: str = field(default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> str:
        """ prints name and age as search string"""
        self._search_string = f"{self.name}, {self.age}"


def main_method() -> None:
    """ initialize and print the data class"""
    person = Person("Marker gini", 23, 34.0980)
    print(person)
    print(person.__dict__["name"])


if __name__ == '__main__':
    main_method()
