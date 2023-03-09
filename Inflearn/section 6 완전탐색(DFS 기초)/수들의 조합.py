import sys

def DFS(L, S, sum):
    global res
    if L == m:
        if sum % k == 0:
            res += 1
    else:
        for i in range(S, n):
            DFS(L+1, i+1, sum+a[i])


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    k = int(input())
    res = 0
    DFS(0, 0, 0)
    print(res)