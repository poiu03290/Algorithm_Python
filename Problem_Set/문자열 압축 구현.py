# 반복되는 문자열을 예시와 같이 압축하는 프로그램을 작성하여라.
# 입력에는 a-z 까지의 문자열만 들어간다.

# 입력 예시
# aaaaabbbbb

# 출력 예시
# a5b5

sentence = str(input()) + " "
char = sentence[0]
count = 1

for i in sentence[1:]:
    if char == i:
        count += 1
    else:
        print(char, end="")
        if count > 1:
            print(count, end= "")
        char = i
        count = 1