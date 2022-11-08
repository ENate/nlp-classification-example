"""Main"""
from dataclasses import dataclass
from functools import partial
from timeit import timeit


@dataclass(slots=False)
class TeacherSlots:
    """printing teachers"""
    name: str
    age: int
    address: str


@dataclass(slots=False)
class Teacher:
    """printing teachers"""
    name: str
    age: int
    address: str


def square(number: int | float) -> int | float:
    return number ** 2


def get_set_delete(Teacher | TeacherSlots):
    """ checking slots and unions"""
    teacher.address = " 5 main street"
    teacher.address
    del teacher.address


def main():
    """Initializing and pring customer obj"""
    teacher = Teacher("Raipert", 23, "6 main street")
    teacher_slots = TeacherSlots("Raipert", 23, "6 main street")
    slots = min(timeit.repeat(
        partial(get_set_delete, teacher), number=1000000))

    no_slots = min(timeit.repeat(
        partial(get_set_delete, teacher_slots), number=1000000))
    print(f"{slots}")
    print("%performance: {(no_slots - slots )/ no_slots:.2%}")
    print(teacher.age)


if __name__ == '__main__':
    main()
