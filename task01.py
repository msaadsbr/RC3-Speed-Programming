# With The Name Of Allah Almighty

import sys
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def stinp(): return str(inp())
def intinp(): return int(inp())
def mapint(): return map(int, inp().split())
def mapst(): return map(str, inp().split())
def listint(): return list(map(int, inp().split()))


for _ in range(intinp()):
    s = stinp()
    if s.isnumeric():

        cnt = str(s.count("7")+s.count("4"))
        if len(set(cnt))>2: print("NO")
        else:
            for i in cnt:
                if i not in ["4","7"]:
                    print("NO")
                    break
            else:
                print("YES")
    else: print("Invalid")

