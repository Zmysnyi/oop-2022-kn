class Employee:

    nums_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.nums_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

emp_1.set_raise_amt(1.05)
print("Процент підвищення першого: ", emp_1.raise_amt)
print("Процент підвищення другого: ", emp_2.raise_amt)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)
print("email працівника, створеного зі строки: ", new_emp_1.email)
print("Зарплата працівника, створеного зі строки: ", new_emp_1.pay)

import datetime

my_date = datetime.date(2016, 7, 10)
print("Дата 2016-7-10 робочий день? ", Employee.is_workday(my_date))
