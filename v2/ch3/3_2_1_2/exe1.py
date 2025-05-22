x=5772156648
a=3141592621
c=2718281829
m=10000000000


def gcd(a, b):
    c = a % b
    if c == 0:
        return b
    return gcd(b, c)

print(f"GCD of c and m is {gcd(c,m)}") 

b = a - 1
print(f"{b} is multiple of 2? {(b%2)==0}")
print(f"{b} is multiple of 5? {(b%5)==0}")


print(f"{b} is multiple of 4? {(b%4)==0}") 

#accourding to Theorem A period length is m=10000000000
