import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    
    n = int(input())
    calc = list(input())
    for i in range(len(calc)-1, -1, -1):
        if calc[i] == '*':
            calc[i], calc[i+1] = calc[i+1], calc[i] 

        if calc[i] == '+':
            calc[i], calc[i+1] = calc[i+1], calc[i]
    print(calc)