n = int(input())
a = list(map(int, input().split()))
max = -2147000000

def digit_sum(x):
    sum = 0
    for j in str(x):
        sum += int(j)
    return sum

for i in a:
    res = digit_sum(i)
    if res > max:
        max = res
        result = i

print(result)