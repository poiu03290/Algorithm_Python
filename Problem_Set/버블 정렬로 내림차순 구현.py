# #1.

# 숫자 n이 주어지고, n 개 만큼 무작위 수(0 <= x <= 100000)가 주어진다. 이를 내림차순으로 정렬하여 출력하여라.

# > 5
# > 22 31 42 50 12
# 50
# 42
# 31
# 22
# 12

# 입력
# 5
# 22
# 31
# 42
# 50
# 12


# 출력
# 50
# 42
# 31
# 22
# 12


n = int(input())
stack = []

for i in range(n):
    k = int(input())
    stack.append(k)

for i in range(1, n):
    for j in range(n-i):
        if stack[j] < stack[j+1]:
            continue
        elif stack[j] > stack[j+1]:
            stack[j], stack[j+1] = stack[j+1], stack[j]

print(stack)
for i in range(len(stack)):
    print(stack.pop())