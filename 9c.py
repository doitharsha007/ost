# 9c) : Write a program to find GCD and LCM of two numbers using functions 

def gcd(one,two):
    factors = list(range(1,min(one,two)+1))
    factors.reverse()
    for i in factors:
        if one % i==0 and two % i==0:
            return i
def lcm(gcd,one,two):
    return int(one*two/gcd) #since gcd * lcm = one * two
one = int(input("Enter first number - "))
two = int(input("Enter second number - "))
gcd = gcd(one,two)
print("GCD of",one,"and",two,"-",gcd)
print("LCM of",one,"and",two,"-",lcm(gcd,one,two))

