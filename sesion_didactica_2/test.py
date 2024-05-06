import random
def prime_number()->int:
    result=0
    while True:
        num = random.randint(1, 100)
        if num > 1:
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    break
            else:
                return num
            


print(prime_number())