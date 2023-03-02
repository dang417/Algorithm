import sys
sys.stdin = open('input.txt')

from itertools import combinations

n = int(input())

stat = [list(map(int, input().split())) for _ in range(n)]
comb = list(combinations(list(range(n)), n//2))
start = comb[:len(comb)//2]
link = comb[len(comb):(len(comb)//2)-1:-1]

rlt = 100000000000
start_stat_list = []
link_stat_list = []
for s in start:
    start_stat = 0
    for i in combinations(s, 2):
        start_stat += stat[i[0]][i[1]] + stat[i[1]][i[0]]
    start_stat_list.append(start_stat)

for l in link:
    link_stat = 0
    for i in combinations(l, 2):
        link_stat += stat[i[0]][i[1]] + stat[i[1]][i[0]]
    link_stat_list.append(link_stat)

for i in range(len(comb)//2):
    if rlt >= abs(start_stat_list[i] - link_stat_list[i]):
        rlt = abs(start_stat_list[i] - link_stat_list[i])

print(rlt)