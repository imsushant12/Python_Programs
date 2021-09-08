def find_gcd(x,y):
    if y == 0:
        return x
    return find_gcd(y , x % y)

 
x = 45
y = 27

print(f"GCD of {x} and {y} is : " + str(find_gcd(x,y)))