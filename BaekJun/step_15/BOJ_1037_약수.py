n = int(input())
factor_list = list(map(int, input().split()))

max_factor = max(factor_list)
min_factor = min(factor_list)

print(max_factor * min_factor)