def mean():
    print("1. Findind the mean value of the dictonary")
    dict1={"A":1 ,"B":2 ,"C":3 ,}
    dict2=sum(dict1.values()) / len(dict1)
    print("The output is=" , dict2)
    
def merge():
    print("2. Merge the three dictonary and create a new dictonary")
    dict3={1:10, 2:20}
    dict4={3:30, 4:40}
    dict5={5:50,6:60}
    dict6={}
    for a in (dict3,dict4,dict5):
        dict6.update(a)
    print("The final output=",dict6)
    
def key_value():
    print("3.Get the key, value and item in a dictionary")
    dict7={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print("\n Keys")
    for b in dict7.keys():
        print("The keys are=", b)
    print("\n Values")
    for c in dict7.values():
        print("The values are=",c)
    print("\n Items")
    for d in dict7.items():
        print("The items are=",d)
        
def employee():
    print("4. Getting the employee information")
    employee_data={
        "10":{"Name":"Sahil","Department":"Web Development", "Salary":20000},
        "20":{"Name":"Sathish","Department":"Software Development", "Salary":30000},
        "30":{"Name":"Suman","Department":"Fullstack Development", "Salary":40000}
        }
    dict8=input("Enter the employee id=")
    if dict8 in employee_data:
        dict9=employee_data[dict8]
        print("Employee data")
        print(f"\nEmployee Name :{dict9['Name']}")
        print(f"Employee Department :{dict9['Department']}")
        print(f"Employee Salary :{dict9['Salary']}")
        

        
        
         
    
mean()
merge()
key_value()
employee()