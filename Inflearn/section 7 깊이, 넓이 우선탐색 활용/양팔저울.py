import sys

def DFS(L, sum):
    if L == n:
        if s >= sum > 0:
            res.add(sum)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum-a[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res = set()
    s = sum(a)
    DFS(0, 0)
    print(s-len(res))