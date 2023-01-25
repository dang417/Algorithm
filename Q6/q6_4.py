t = int(input())
for i in range(t):
    r, s = input().split()
    s_sep = []
    for j in range(len(s)):
        s_sep.append(s[j])
        print(s_sep[j]*int(r), end='')
    print() 
    #마지막에 print() 를 해줘야 줄바꿈이 일어난다