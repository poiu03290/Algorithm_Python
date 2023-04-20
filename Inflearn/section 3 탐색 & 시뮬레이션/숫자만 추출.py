s = input()
res = ''
cnt = 0

for i in s:
    if i.isdigit():
        res += i

res = int(res)

for i in range(1, res+1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)