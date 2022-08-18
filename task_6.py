from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Person:
    name: str
    surname: str
    age: int
