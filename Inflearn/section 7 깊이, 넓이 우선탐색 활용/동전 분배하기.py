import sys

def DFS(L):
    global res
    if L == n:
        cha = max(m) - min(m)
        if res > cha:
            tmp = set()
            for i in m:
                tmp.add(i)
            if len(tmp) == 3:
                res = cha
    else:
        for i in range(3):
            m[i] += a[L]
            DFS(L+1)
            m[i] -= a[L]


if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    m = [0] * 3
    res = 2147000000
    DFS(0)
    print(res)