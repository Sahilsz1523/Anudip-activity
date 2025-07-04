def add_remove():
    print("1.Adding and removing the person name")
    students=["Rahul", "Aisha", "Meena"]
    students.append("Sathish")
    print("After adding:",students)
    students.remove("Aisha")
    print("After Removing:",students)

def even():
    print("2. Adding even number in the list")
    even_numbers=[a for a in range(1,21) if a % 2==0]
    print("Even numbers=",even_numbers)

def averege():
    print("3.Finding averege number from the list")
    numbers=[10 ,20 ,30 ,40]
    averege=sum(numbers)/ len(numbers)
    print("Averege is=" ,averege)

def product():
    print("4. Finding the product is in the cart or not")
    cart=["shoes", "watch", "phone", "wallet"]
    product=input("Enter the product name:").lower()
    
    if product in cart:
        print(f"{product.title()} is avaible in the cart")
    else:
        print(f"{product.title()} is not avaible in the cart")

def counting():
    print("5.Checking how many time the name appears in the list")
    names = ["Arun", "Meena", "Arun", "Ravi", "Arun", "Meena"]
    check=input("Enter the name:")
    a=names.count(check)
    print("Total appearence=",a)

def length():
    print("Splitting the length of the list")
    real_list=[1, 1, 2, 3, 4, 4, 5, 1]
    first_list_length=3
    
    firstlist=real_list[:first_list_length]
    secondlist=real_list[first_list_length:]
    
    print("original list=",real_list)
    print("First list",firstlist)
    print("Second list",secondlist)
    
    
    





add_remove()
even()
averege()
product()
counting()
length()

