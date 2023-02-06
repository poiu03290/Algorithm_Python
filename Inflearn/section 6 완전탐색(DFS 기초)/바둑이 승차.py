import sys

def DFS(L, sum, tsum):
    global res
    if res > (total-tsum) + sum:
        return 
    if sum > n:
        return
    if L == m:
        if res < sum:
            res = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(int(input()))
    total = sum(a)
    res = 0
    DFS(0, 0, 0)
    print(res)