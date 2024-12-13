# With The Name Of Allah Almighty

import sys
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def stinp(): return str(inp())
def intinp(): return int(inp())
def mapint(): return map(int, inp().split())
def mapst(): return map(str, inp().split())
def listint(): return list(map(int, inp().split()))

from collections import deque

def solve(mat, i, j, req):
    pos = [(0,1),(0,-1),(1,0),(-1,0)]
    st = mat[i][j]
    q = deque([(i,j,st,[(i,j)])])
    while q:
        r,c,val,lst = q.popleft()
        if val == req:
            return True
        for R,C in pos:
            nr,nc = r+R,c+C
            if 0<=nr<3 and 0<=nc<4 and (nr,nc) not in lst and (len(val)) < len(req):
                q.append((nr,nc,val+mat[nr][nc],lst+[(nr,nc)]))
    return False

st = []
for i in range(3): st.append(stinp())
words = []
for j in range(intinp()): words.append(stinp())
for word in words:
    flag = False
    for i in range(3):
        for j in range(4):
            if st[i][j]==word[0]:
                if (solve(st,i,j,word)): flag = True
    print(flag)









