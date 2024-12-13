# With The Name Of Allah Almighty


import sys
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def stinp(): return str(inp())
def intinp(): return int(inp())
def mapint(): return map(int, inp().split())
def mapst(): return map(str, inp().split())
def listint(): return list(map(int, inp().split()))

mx = [float('inf'),-1]
mn = [float('inf'), float('inf')]
for _ in range(intinp()):
    ip = stinp().split()
    if ip[0]=="INSERT":
        score = int(ip[2])
        id = int(ip[1])
        if (mx[1]==score and id<mx[0]) or score>mx[1]:
            mx = [id, score]
        if (mn[1]==score and id<mn[0]) or score<mn[1]:
            mn = [id, score]
    else:
        if ip[0]=="Highest": print(mx[0])
        else: print(mn[0])

