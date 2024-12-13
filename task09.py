# With The Name Of Allah Almighty

import sys
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def stinp(): return str(inp())
def intinp(): return int(inp())
def mapint(): return map(int, inp().split())
def mapst(): return map(str, inp().split())
def listint(): return list(map(int, inp().split()))

employees = [[[1,2],[4,5]],[[2,3],[5,6]],[[3,4]]]
lst = []
for employee in employees:
    for job in employee:
       lst.extend(list(range(job[0],job[1])))
lst = list(set(lst))
lst.sort()
i = 0
ans = []
while i<len(lst)-1:
    if lst[i+1]-lst[i]!=1: ans.append([lst[i]+1,lst[i+1]])
    i += 1
print(ans)








