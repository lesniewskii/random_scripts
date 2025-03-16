n = int(input())
magnets = [input().strip() for _ in range(n)]

groups = 1  # At least one group exists
for i in range(1, n):
    if magnets[i] != magnets[i - 1]:
        groups += 1

print(groups)


