import sys

def DFS(L, P):
    global res
    if L == n+1:
        if res < P:
            res = P
    else:
        if L+a[L][0]<=n+1:
            DFS(L+a[L][0], P+a[L][1])
        DFS(L+1, P)

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        t, p = map(int, input().split())
        a.append((t, p))
    res = 0
    a.insert(0, (0, 0))
    DFS(1, 0)
    print(res)