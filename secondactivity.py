print("1.Using ternary operator")
def ternary():
    var1=int(input("enter the number"))
    var2="even" if var1 % 2==0  else "odd"
    print(var2)

print("2.swap the number")
def swap():
    var3=int(input("Enter the first number"))
    var4=int(input("Enter the second number"))
    
    var5=var3
    var3=var4
    var4=var5
    
    print("var3=" ,var3)
    print("var4=" ,var4)

print("3.Km to miles")
def miles_km():
    km=float(input("Enter the km"))
    miles=km*0.621371
    print(f"{km} km is equal to {miles:.2f}miles")


print("4.Simple intrest")
def simpleintrest():
    p=20000
    r=5
    t=3
    SI=(p*t*r)/100
    print(SI)
    
    
ternary()
swap()
miles_km()
simpleintrest()


    



