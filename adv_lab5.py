class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def transfer_money(self, other_account, amount):
        if isinstance(other_account, BankAccount) and 0 < amount <= self.__balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"Transferred {amount} to account {other_account.__account_number}")
        else:
            print("Transfer failed. Check amount and account validity.")

acc1 = BankAccount("12345")
acc2 = BankAccount("67890")

acc1.deposit(1000)
acc1.withdraw(200)
print("Balance acc1:", acc1.get_balance())

try:
    print(acc1.__balance)
except AttributeError as e:
    print("Cannot access private attribute directly:", e)

acc1.transfer_money(acc2, 300)
print("Balance acc1:", acc1.get_balance())
print("Balance acc2:", acc2.get_balance())

class Product:
    def __init__(self, price):
        self._price = None
        self.price = price  

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")

    @price.deleter
    def price(self):
        print("Deleting price...")
        self._price = None

p = Product(500)
print("Initial price:", p.price)

try:
    p.price = -100
except ValueError as e:
    print("Setting negative price error:", e)

del p.price
print("After deletion, price:", p.price)

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_employee_details(self):
        pass

    @abstractmethod
    def raise_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def get_employee_details(self):
        return f"Full-time: {self.name}, ID: {self.emp_id}, Salary: {self.calculate_salary()}"

    def raise_salary(self):
        self.monthly_salary *= 1.10

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_employee_details(self):
        return f"Part-time: {self.name}, ID: {self.emp_id}, Salary: {self.calculate_salary()}"

    def raise_salary(self):
        self.hourly_rate *= 1.05

ft = FullTimeEmployee("Alice", "FT001", 50000)
pt = PartTimeEmployee("Bob", "PT002", 200, 100)

print(ft.get_employee_details())
print(pt.get_employee_details())

ft.raise_salary()
pt.raise_salary()

print("After raise:")
print(ft.get_employee_details())
print(pt.get_employee_details())

class SmartDevice:
    def __init__(self, name, battery_level):
        self.name = name
        self.__is_on = False
        self.battery_level = battery_level

    def turn_on(self):
        if self.battery_level > 20:
            self.__is_on = True
            print(f"{self.name} is now ON")
        else:
            print(f"{self.name} battery too low to turn on!")

    def turn_off(self):
        self.__is_on = False
        print(f"{self.name} is now OFF")

    @property
    def is_on(self):
        return self.__is_on

    @is_on.setter
    def is_on(self, status):
        if status and self.battery_level <= 20:
            print("Cannot turn on device due to low battery.")
        else:
            self.__is_on = status


device = SmartDevice("Smart Light", 15)
device.turn_on()  
device.battery_level = 80
device.turn_on()   
print("Device status:", device.is_on)
device.turn_off()
print("Device status:", device.is_on)



