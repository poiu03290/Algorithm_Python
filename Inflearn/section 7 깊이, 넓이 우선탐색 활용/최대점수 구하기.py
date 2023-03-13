import sys

def DFS(L, S, T):
    global res
    if T > m:
        return
    if L == n:
        if res < S:
            res = S
    else:
        DFS(L+1, S+a[L][0], T+a[L][1])
        DFS(L+1, S, T)

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        s, t = map(int, input().split())
        a.append((s, t))
    res = 0
    DFS(0, 0, 0)
    print(res)
