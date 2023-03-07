import sys

def DFS(L, sum):
    if L == n:
        if sum == m:
            for i in p:
                print(i, end=' ')
            sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, sum+(i*b[L]))
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n+1)
    b = [1] * n
    p = [0] * n
    for i in range(1, n):
        b[i] = b[i-1]*(n-i) //i
    DFS(0, 0)
