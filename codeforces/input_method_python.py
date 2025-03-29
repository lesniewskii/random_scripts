#Fast Input Handling (Codeforces)
import sys
data = sys.stdin.read().split()
print(data)  # ['5', '10', '20', '30', '40', '50']

n = int(data[0])  # 5
arr = list(map(int, data[1:n+1]))  # [10, 20, 30, 40, 50]

#Input with Space-Separated Integers
arr = list(map(int, input().split()))

#Multiple lines of integers
arr = [int(input()) for _ in range(n)]

#Single integer input
n = int(input())

#Single line of space-separated integers
arr = list(map(int, input().split()))

#Input with Mixed Data Types
n, f, s = input().split()
n = int(n)
f = float(f)