import sys

def DFS(v):
    global res
    if v == n:
        res += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0 and g[v][i] == 1:
                ch[i] = 1
                DFS(i)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    res = 0
    ch[1] = 1
    DFS(1)
    print(res)