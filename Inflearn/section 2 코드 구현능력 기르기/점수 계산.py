n = int(input())
a = list(map(int, input().split()))
res = 0
tmp = 0

for i in range(n):
    if a[i] == 1:
        tmp += 1
        res += tmp
    else:
        tmp = 0

print(res)