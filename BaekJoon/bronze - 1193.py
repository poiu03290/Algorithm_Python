n = int(input())
line = 0
end_num = 0

while n > end_num:
    line += 1
    end_num += line

diff = end_num - n

if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print('{0}/{1}'.format(top, bottom))