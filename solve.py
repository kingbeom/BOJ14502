from collections import deque
import copy
from itertools import combinations
def bfs(i):
    mapp2=copy.deepcopy(mapp)
    dq=deque()
    sol=0
    for t in range(len(i)):
        y,x=i[t]
        mapp2[y][x]=1
    for y in range(n):
        for x in range(m):
            if mapp2[y][x]==2:
                dq.append([y,x])
    while dq:
        y,x=dq.popleft()
        for t in range(4):
            ny,nx=y+dy[t],x+dx[t]
            if 0<=ny<n and 0<=nx<m and mapp2[ny][nx]==0:
                mapp2[ny][nx]=2
                dq.append([ny,nx])
    for k in mapp2:
        sol+=k.count(0)
    return sol
n,m=map(int, input().split())
mapp=[list(map(int, input().split())) for _ in range(n)]
dy,dx=[0,0,1,-1],[1,-1,0,0] # 동 서 남 북
lst=[]
chk=[]
for i in range(n):
    for j in range(m):
        if mapp[i][j]==0:
            lst.append([i,j])
for i in combinations(lst, 3):
    chk.append(bfs(i))
print(max(chk))