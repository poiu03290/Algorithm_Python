n = int(input())
res = 0
for i in range(n):
    tmp = 0
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] == a[2]:
        tmp = 10000 + (a[0] * 1000)
    elif a[0] == a[1] or a[1] == a[2]:
        tmp = 1000 + (a[1] * 100)
    else:
        tmp = a[2] * 100
    if tmp > res:
        res = tmp

print(res)