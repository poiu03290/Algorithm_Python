a = list(range(0, 21))

for i in range(10):
    s, e = map(int, input().split())
    for j in range((e-s+1)//2):
        a[s+j], a[e-j] = a[e-j], a[s+j]
    
a.pop(0)
for i in a:
    print(i, end=' ')