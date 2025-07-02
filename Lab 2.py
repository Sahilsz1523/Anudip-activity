
def div(a,b):
    print("1. Uding div passing two parameters")
    try:
        if b!=0:
            print("Divition is:", a/b)
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print("Zero Divition Error")


def square(c):
    print("2.Declare square with one parameter")
    print("square=", c*c)

def random():
    print("3.Print max and min of 5 random numbers")
    import random
    numbers=[random.randint(1,100) for d in range(5)]
    print("Random numbers:" ,numbers)
    print("Max:", max(numbers))
    print("Min:", min(numbers))

def lower():
    print("4.Accept a name and display in lower case")
    name=input("Enter the name:")
    print("name=", name.lower())
    
div(10,5)
square(5)
random()
lower()

e=int(input("Enter the number:"))
check_number = lambda e: "Positive" if e > 0 else ("Zero" if e == 0 else "Negative")
print(check_number(e))




    