# +, - 연산자만을 활용하는 계산기를 만들어라

# 예시 입력1
# 1+2+3-2

# 예시 출력1
# 4

# 예시 입력2
# 1-5+220+1+2

# 예시 출력2
# 219


import re
input = str(input())
splitInput = re.split(r'\+|-', input)
operatorIndex = []
result = 0

if input[0] != '-':
    input = '+' + input[0:]
elif input[0] == '-':
    del splitInput[0]

for i in range(len(input)):
    if input[i] == '+' or input[i] == '-':
        operatorIndex.append(i)

for i in range(len(splitInput)):
    try:
        result += int(input[operatorIndex[i]:operatorIndex[i+1]])
    except IndexError:
        result += int(input[operatorIndex[i]:])
print(result)