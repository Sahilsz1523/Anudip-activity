def palindrome():
    print("1. Check the string is palindrome or not")
    a=input("Enter the word:")
    if a==a[::-1]:
        print("The word is palindrome")
    else:
        print("The word is not palindrome")

def vowel():
    print("2.counting a vowel in the sentence")
    b=input("Enter the sentence:")
    vowels=['a','e','i','o','u']
    count=0
    
    for char in b.lower():
        if char in vowels:
            count+=1
            print(char)


def replace():
    c=input("enter the sentence:")
    d=(c.replace(" ","-"))
    print("The final sentence",d)

def check_password():
    password=input("enter the password=")
    return (len(password)>=8 and any (char.isupper() for char in password)
            and (char.islower() for char in password))


def extract():
    email=input("Enter the email")
    if "@" in email:
        domain=email.split("@")[1]
        print("Domain=",domain)
    else:
        print("No domain")
        
        
vowel()
palindrome()
replace()
check_password()
extract()


                
    