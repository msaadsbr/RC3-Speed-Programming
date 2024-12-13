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
    if s.isalpha():
        s = s.lower()
        print("Female" if len(set(s))&1==0 else "Male")
    else: print("Invalid")
