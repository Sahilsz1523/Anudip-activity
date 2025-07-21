def prime_numbers():
    print("1. Using generator printing the prime numbers")
    num=2
    while True:
        is_prime= True
        for a in range(2,int(num**0.5) +1):
            if num%a==0:
                is_prime= False
                break
        if is_prime:
            yield num
        num+=1
            
prime_gen=prime_numbers()
for _ in range(15):
    print(next(prime_gen),end=' ')
    
def temprature():
    import random
    print("Before")
    print("\n2. Finding the temperature using generator")
    while True:
        yield round(random.uniform(-10,30),2)
        
temp_gen=temprature()
for _ in range(10):
    print(f"temprature=:{next(temp_gen)}")
    
    
def fibonacci():
    print("\n3. Finding the fibonacci using generator")
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
def sum_fibo(c):
    sum_fibonacci=fibonacci()
    return sum(next(sum_fibonacci) for _ in range(c))
print("The sum of the fibonacci series=",sum_fibo(10))

def filter_strings(data):
    print("\n4. Finding the string from the mixed data using generator")
    for item in data:
        if isinstance(item, str):
            yield item
mixed_data = [1, "hello", 3.14, "world", 42]
string_gen = filter_strings(mixed_data)
for s in string_gen:
    print(s)
