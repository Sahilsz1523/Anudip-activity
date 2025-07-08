def union_set():
    print("1. find the unique element")
    set1={1,2,3,4,5}
    set2={1,2,3,4,5}
    set3=set1.union(set2)
    print("The unique numbers are=", set3)

def difference_set():
    print("2.Finding the difference of the two sets")
    set4={6,8,9,2,4}
    set5={1,2,3,4,6}
    set6=set4.difference(set5)
    print("the final output=", set6)
    
def intersect_set():
    print("3.Finding the common value")
    set7={6,8,9,2,4}
    set8={1,2,3,4,6}
    set7.intersection(set8)
    print("The common result=",set8)

def visitor_list():
    print("4.Finding the visitor of the website")
    number=int(input("Enter how many visitor visited the website="))
    visitor=set()
    for i in range(number):
        name=input(f"Enter visitor {i+1} : name or id").strip()
        if name:
            visitor.add(name.lower())
    print("\nUnique visitor")
    for a in visitor:
        print(a.title())
        print("The total number of unique visitor=",len(visitor))
        
def hobbies():
    print("5.Find the common hobbies of two frineds")
    friend1=input("Enter the hobbies of friend 1 ,(commo-seprate)")
    friend2=input("Enter the hobbies of friend 2 ,(commo-seprate)")
    set9=set(frnd.strip() for frnd in friend1.split(",") if frnd.strip())
    set10=set(frnd.strip() for frnd in friend2.split(",") if frnd.strip())
    
    print("\n the common hobbies are")
    print("common hobbies=",",".join(set9 & set10) or "None")
    print("All hobbies=" ,",".join(set9|set10))
    print("Friend 1 hobbies=" ,",".join(set9-set10) or "None")
    print("Friend 2 hobbies=" ,",".join(set10-set9) or "None")
    
                
union_set()
difference_set()
intersect_set()
visitor_list()
hobbies()
    