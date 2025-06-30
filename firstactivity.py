def oddeven():
    print("1.check the number is even or odd")
    num=int(input("Enter the number:"))
    if num % 2==0:
        print("Even number")
    else:
        print("Odd Number")

def marks():
    print("2. Average and Grade Calculation")
    marks = []

    for i in range(1, 6):
        mark = int(input(f"Enter marks {i}: "))
        marks.append(mark)

    if any(m < 35 for m in marks):
        print("Status: Fail\n")
    else:
        avg = sum(marks) / 5
        print("Average:", avg)

        if avg >= 90:
            print("Grade: A")
        elif avg >= 70:
            print("Grade: B")
        elif avg >= 50:
            print("Grade: C")
        elif avg >= 35:
            print("Grade: D")
        else:
            print("No grade")
        
def primenumber():
    print("3.Checking the number is prime number or not")
    n=int(input("Enter the number"))
    if n>1:
        for i in range(2,n):
            if n % i==0:
                print("This is not a prime number\n")
                break
            else:
                print("the number is prime number")
                
    else:
        print("THis number is not prime number")
        
        
def studentdetail():
    print("4. print student details")
    id=int(input("Enter student id="))
    name=input("Enter student name=")
    age=int(input("Enter student age="))
    city=input("Enter city=")
    phone=int(input("Enter phone="))
    
    print("id=" , id)
    print("name=" , name)
    print("age=" , age)
    print("city=", city)
    print("phone=", phone)
    
    
    
oddeven()
marks()
primenumber()
studentdetail()
        
    
    
        