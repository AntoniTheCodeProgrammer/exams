import math

def table(T):
    for i in range(2, 101):
        T.append(i)

def primes(T):
    n = int(math.sqrt(max(T)))   
    result = []
    for i in T:
        k = 0
        for j in range(2, n):
            if i % j == 0 and i != j:
                k += 1
        if k == 0:
            result.append(i)  
    return result

T = []
table(T)
print(T)
print(primes(T))