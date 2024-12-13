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
    for i in s:
        if ord(i)<97:
            print("Incorrect Input")
            break
    else:
        if len(s)<=10:
            print(s)
        else:
            print(s[0] + str(len(s)-2) +s[-1])