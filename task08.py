# With The Name Of Allah Almighty

import sys
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def stinp(): return str(inp())
def intinp(): return int(inp())
def mapint(): return map(int, inp().split())
def mapst(): return map(str, inp().split())
def listint(): return list(map(int, inp().split()))

def check(st):
    s = st.split(".")
    if len(s)!=4: return False
    for i in s:
        p = int(i)
        if p<0 or p>255: return False
        if i[0]=="0" and len(i)>1: return False
    return True
for _ in range(intinp()):
    ans = []
    s = stinp()
    if len(s)<4 or not s.isnumeric(): print([])
    else:
        for i in range(1,len(s)-3):
            for j in range(i+1,len(s)-2):
                for k in range(j+1, len(s)-1):
                    st = s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:]
                    if check(st):
                        ans.append(st)

        print(ans)




