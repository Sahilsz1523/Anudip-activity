
class Vehicle:
    def __init__(self, registration_number, brand, rental_price_per_day):
        self.registration_number = registration_number
        self.brand = brand
        self.rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days
class Car(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, insurance_fee):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.insurance_fee = insurance_fee

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost + self.insurance_fee
class Bike(Vehicle):
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)  
class Truck(Vehicle):
    def __init__(self, registration_number, brand, rental_price_per_day, load_charge):
        super().__init__(registration_number, brand, rental_price_per_day)
        self.load_charge = load_charge

    def calculate_rental_cost(self, days):
        base_cost = super().calculate_rental_cost(days)
        return base_cost + self.load_charge
    
c = Car("TN10AB1234", "Hyundai", 1500, insurance_fee=500)
b = Bike("TN22XY7890", "Honda", 500)
t = Truck("TN07GH5678", "Tata", 2500, load_charge=800)

print("Car rental (3 days):", c.calculate_rental_cost(3))
print("Bike rental (3 days):", b.calculate_rental_cost(3))
print("Truck rental (3 days):", t.calculate_rental_cost(3))



class User:
    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

    def login(self):
        print(f"{self.name} logged in with email {self.email}")
class Teacher(User):
    def create_course(self, course_name):
        print(f"Teacher {self.name} created course: {course_name}")

    def login(self):
        print(f"Teacher {self.name} logged in.")
class Student(User):
    def enroll_course(self, course_name):
        print(f"Student {self.name} enrolled in course: {course_name}")

    def login(self):
        print(f"Student {self.name} logged in.")

t = Teacher("Alice", "alice@edu.com", "T101")
s = Student("Bob", "bob@edu.com", "S202")

t.login()
t.create_course("Python OOP")

s.login()
s.enroll_course("Python OOP")



