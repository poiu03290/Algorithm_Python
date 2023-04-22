import sys
read = lambda: sys.stdin.readline().rstrip()
n, m = map(int, read().split())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

ap = 0
bp = 0

res = []
while ap < n and bp < m:
    if a[ap] > b[bp]:
        res.append(b[bp])
        bp += 1
    else:
        res.append(a[ap])
        ap += 1

if ap < n:
    res = res + a[ap:]
elif bp < m:
    res = res + b[bp:]

for i in res:
    print(i, end = ' ')

