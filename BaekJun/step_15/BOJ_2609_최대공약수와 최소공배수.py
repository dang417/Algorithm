a, b = map(int, input().split())

def gcd_r(a,b) :
    if b == 0 :
        return a
    else :
        return gcd_r(b,a%b)

def gcd_for(a,b) :
    while b > 0 :
        tmp = a % b
        a = b
        b = tmp
    return a

def lcm(a,b) :
    return a*b//gcd_r(a,b)

print(gcd_r(a,b))
print(lcm(a,b))