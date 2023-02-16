n = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse = True)

for i in range(len(trees)):
    trees[i] += i + 2

print(max(trees))