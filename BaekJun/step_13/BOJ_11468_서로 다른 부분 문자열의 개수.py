s = input()
rlt = []

for i in range(len(s)):
    for j in range(len(s)-i):
        rlt.append(s[j:j+i+1])

print(len(set(rlt)))