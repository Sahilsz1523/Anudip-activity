def counting():
    print("1.Counting the multiple numbers in the tuple")
    tuplea=(2,3,4,5,6,2,2,3,4,4,5,6,)
    b=tuplea.count(4)
    print("Number of same element=",b)
    
def convert():
    listc=[1,2,3,4,5,6,7]
    d=tuple(listc)
    print("tuple=",d)
    
def sum_tuple():
    print("3.Sum the tuple_list")
    tuple_list=[(1,2),(1,2),(1,2)]
    e=sum(sum(f) for f in tuple_list)
    print("Sum of the tuple =",e)
    
def employee():
    employee1=("Sahil","23","web developer",20000)
    employee2=("Sathish","21","Business",50000)
    employee3=("Bhavan","07","Teaching",30000)
    employees = [employee1, employee2, employee3]
    for g in employees:
        print("Employees Record:")
        print(f"Name: {g[0]}")
        print(f"ID: {g[1]}")
        print(f"Role: {g[2]}")
        print(f"Salary: {g[3]}")
        print()
    
def billing():
    print("Creating a product billing section")
    products = []
    total_amount = 0.0  
    number = int(input("Enter the number of products: "))
    for h in range(1, number + 1):
        name = input(f"Enter the name of product {h}: ")
        price = float(input(f"Enter the price of {name}: "))
        quantity = int(input(f"Enter the quantity of {name}: "))
        product = (name, price, quantity)
        products.append(product)

    print("\n<----- Bill Details ----->")

    for product in products:
        name, price, quantity = product
        total = price * quantity
        total_amount += total
        print(f"{name}: {price} x {quantity} = {total}")
    print(f"\nTotal Amount to Pay: {total_amount}")

    
                
    
counting()
convert()
sum_tuple()
employee()
billing()
