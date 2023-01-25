import math

a, b, v = map(int,input().split())

x = ((v-a)/(a-b)) + 1

print(math.ceil(x))
