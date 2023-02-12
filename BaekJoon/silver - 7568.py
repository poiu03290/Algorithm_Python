n = int(input())
body = []

for i in range(n):
    person = input()
    body.append(person.split(' '))

for i in body:
    rank = n
    for j in body:
        if i[0] == j[0] or i[1] == j[1]:
            continue
        elif i[0] > j[0] or i[1] > j[1]:
            rank -= 1
    print(rank, end=' ')