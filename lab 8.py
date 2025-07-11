def marks():
    print("1. Finding the exception of marks below 0 and above 100")
    try:
        marks=int(input("Enter the number of marks:"))
        for a in range(1,marks+1):
            marks_list=int(input(f"Enter the mark of the subjects {a}:"))
            if marks_list<=0 or marks_list>100:
                raise ValueError("invalid Marks , The mark should be more than zero and less than 100")
    except ValueError as e:
        print("Error:",e)
        
def Email():
    print("Finding the exception of the Email")
    try:
        email=input("Enter the email")
        if "@" or "." not in email:
            raise ValueError("Invalid email format")
    except ValueError as e:
        print("Error:" ,e)
    
    
def login():
    print("Using exception on the login attempts")
    try:
        username="sahil"
        password="1923"
        
        for attempt in range(1,4):
            user=input("Enter the username=")
            pass_=input("Enter the password=")
            
            if username==user and password==pass_:
                print("Login Sucessfull")
                break
            else:
                print(f"Attempt {attempt} failed .try again\n")
                
            if attempt==3:
                raise PermissionError("No more attempts avaible")
    except PermissionError as e:
        print("Error:" , e)
        
def Password():
    print("4. checking the password is atleast 8 charcters")
    try:
        password=input("Enter the password")
        if len(password)>8:
            print("Password accepted")
        elif len(password)<8:
            raise ValueError("Week password")
    except ValueError as e:
        print("Error:" , e)
        
def class_exception():
    print("5.class NegativeNumberError and raise it if user inputs a negative number")
    class NegativeNumberError(Exception):
        pass
    def possitive():
        try:
            number=int(input("Enter the possitive number you want ="))
            if number>=0:
                print("The number is possitive number")
            else:
                raise NegativeNumberError("Negative number is not acceptable")
        except NegativeNumberError as e:
            print("Error" , e )

    possitive()    
    
        
        
marks()
Email()
login()
Password()
class_exception()
        