def ispossible(x, y, m, vis, n):
    if ((x >= 0 and x < n) and (y >= 0 and y < n) and m[x][y] == 1 and vis[x][y] == 0):
        return True
    else:
        return False


def solve( m, vis, l, x, y, r, n):
    if (x == n-1 and y == n-1):
        l.append(''.join(r))
        return
    else:
        vis[x][y] = 1
        # DOWN
        newx = x+1
        newy = y
        if (ispossible(newx, newy, m, vis, n)):
            r.append('D')
            solve(m, vis, l, newx, newy, r, n)
            r.pop()
        # UP
        newx = x-1
        newy = y
        if (ispossible(newx, newy, m, vis, n)):
            r.append('U')
            solve(m, vis, l, newx, newy, r, n)
            r.pop()
       # LEFT
        newx = x
        newy = y-1
        if (ispossible(newx, newy, m, vis, n)):
            r.append('L')
            solve(m, vis, l, newx, newy, r, n)
            r.pop()
        # RIGHT
        newx = x
        newy = y+1
        if (ispossible(newx, newy, m, vis, n)):
            r.append('R')
            solve(m, vis, l, newx, newy, r, n)
            r.pop()
        vis[x][y] = 0

def findPath(m, n):
    # code here
    vis = []
    r = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(0)
        vis.append(a)
    l = []
    if (m[0][0] == 0):
        return -1
    x, y = 0, 0
    solve(m, vis, l, x, y, r, n)
    return l
a=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
n=4
print(findPath(a,n))

