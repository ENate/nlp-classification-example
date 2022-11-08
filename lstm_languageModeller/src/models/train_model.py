"""Basic training file for all models"""


class Customer:
    """Exploring the meaning of data and behaviorial classes"""

    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    # add str method
    def __str__(self) -> str:
        return f"The salary is: {self.salary}, \n and age is: {self.age}"

    def calculate_pay(self) -> float:
        """ calculates pay for customer"""
        return self.salary + self.age * 2

    def safe_pay(self) -> float:
        """ calculates pay for customer"""
        return self.salary


def main() -> None:
    """Initializing and pring customer obj"""
    customer = Customer("Raipert", 23, 23.000)
    print(customer)
    print(customer.age)


if __name__ == '__main__':
    main()
