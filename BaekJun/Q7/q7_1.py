import sys

a,b,c = map(int,sys.stdin.readline().split())
if c-b <= 0 :
    print(-1)
else :
    print(int(a/(c-b)+1))