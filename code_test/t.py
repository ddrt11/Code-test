def prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

print("100以内的素数有：")
for i in range(2, 100):
    if prime(i):
        print(i,end=" ")