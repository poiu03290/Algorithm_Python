import sys
input = sys.stdin.readline

def DFS(L, sum):
    global cnt
    if sum > m:
        return
    if L == n:
        if sum == m:
            cnt += 1
    else:
        for i in range(b[L]+1):
            DFS(L+1, sum+a[L]*i)

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        s, p = map(int, input().split())
        a.append(s)
        b.append(p)
    cnt = 0
    DFS(0, 0)
    print(cnt)