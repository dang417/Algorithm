import sys
sys.stdin = open('input.txt', encoding='utf-8')


for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    count = 0
    p_idx = 0
    for t_idx in range(len(target) - len(pattern)+1):
        if p_idx and t_idx + p_idx <= last_t_idx + len(pattern):
            continue

        for p_idx in range(len(pattern)):
            if pattern[p_idx] != target[t_idx + p_idx]:
                # last_t_idx = t_idx
                p_idx = 0
                break
        else:
            count += 1
            last_t_idx = t_idx
    print(count, target.count(pattern))