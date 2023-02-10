n, m = map(int,input().split())
no_hear = {input() for i in range(n)}
no_see = {input() for i in range(m)}

no_hear_no_see = sorted(list(no_hear & no_see))

print(len(no_hear_no_see))

for i in range(len(no_hear_no_see)):
    print(no_hear_no_see[i])