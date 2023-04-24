n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
sum = a[0]
cnt = 0

while True:
    if sum == m:
        cnt += 1
        sum -= a[lt]
        lt += 1
    elif sum < m:
        if rt < n:
            sum += a[rt]
            rt += 1
        else:
            break
    else:
        sum -= a[lt]
        lt += 1
        
print(cnt)