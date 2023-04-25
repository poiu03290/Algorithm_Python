n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
tmp = 0
tmp1 = 0

for i in range(n):
    width = 0
    len = 0
    tmp += a[i][i]
    tmp1 += a[i][n-1-i]
    for j in range(n):
        width += a[i][j]
        len += a[j][i]
    if width > res:
        res = width
    if len > res:
        res = len
    if tmp > res:
        res = tmp
print(res)