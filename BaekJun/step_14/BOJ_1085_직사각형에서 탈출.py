x, y, w, h = map(int,input().split())

print(min(x, abs(x-w), y, abs(y-h)))