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
    exp = stinp()

    i = len(exp)-1
    while i >=0:
        if exp[i]=="*":
            s = s.rstrip(exp[i-1])
            i -= 1
        elif exp[i]==".":
            s = s[:-1]
        else:
            if s[-1]==exp[i]:
                s = s[:-1]
            else:
                print(0)
                break
        i -= 1
    else:
        print(True if s=="" else 0)





