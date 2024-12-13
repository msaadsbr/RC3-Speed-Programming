# With The Name Of Allah Almighty

import sys
input = sys.stdin.read
def inp(): return sys.stdin.readline().strip()
def stinp(): return str(inp())
def intinp(): return int(inp())
def mapint(): return map(int, inp().split())
def mapst(): return map(str, inp().split())
def listint(): return list(map(int, inp().split()))


def solve(mat, filter, i, j):
    sm  = 0
    sm += filter[0][0]*mat[i-1][j-1] + filter[0][1]*mat[i-1][j] + filter[0][2]*mat[i-1][j+1]
    sm += filter[1][0]*mat[i][j-1] + filter[1][1]*mat[i][j] + filter[1][2]*mat[i][j+1]
    sm += filter[2][0]*mat[i+1][j-1] + filter[2][1]*mat[i+1][j] + filter[2][2]*mat[i+1][j+1]
    return sm//9

n = intinp()
mat = []
for i in range(n): mat.append(listint())
filter = []
m = intinp()
for i in range(m): filter.append(listint())
result = [[0 for i in range(n)] for i in range(5)]
for i in range(1,n-1):
    for j in range(1,n-1):
        result[i][j] = solve(mat, filter, i, j)
print(result)









