import sys

def DFS(L, P):
    global cnt
    if L == n:
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
        cnt += 1 
    else:
        for i in range(1, 27):
            if i == a[L]:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and a[L] == i//10 and a[L+1] == i%10:
                res[P] = i
                DFS(L+2, P+1)

if __name__ == "__main__":
    a = list(map(int, input()))
    n = len(a)
    cnt = 0
    res = [0] * (n+3)
    DFS(0, 0)
    print(cnt)