
def move(x,y,dir):
    if dir == 'U':
       if x-1 >= 0 and grid[x-1][y] == 0:
             return x-1,y
       else:
             return False
    elif dir == 'D':
       if x+1 < m and grid[x+1][y] == 0:
             return x+1,y
       else:
             return False 

    elif dir == 'L':
       if y-1 >= 0 and grid[x][y-1] == 0:
             return x,y-1
       else:
             return False

    elif dir == 'R':
       if y+1 < n and grid[x][y+1] == 0:
             return x,y+1
       else:
             return False


def DFS(x,y,k):
    global flag
#    print k
    if grid[x][y] == 1:
#        print "x , y,1"
        return False
    if x < 0 or x >m-1 or y<0 or y > n-1:
 #       print "x,y not in m,n"
        return False
    if k == step:
        flag = True
#        print flag
        return True
    for i in range(int(trip[k][0])-1):
        tmp = move(x,y,trip[k][2])
        if tmp:
            x,y = tmp
#            print "%d %d" %(x,y)
    for i in range(int(trip[k][0]),int(trip[k][1])+1):
          tmp = move(x,y,trip[k][2])
          if tmp:
               x,y = tmp
#               print "%d %d" %(x,y)
               DFS(x,y,k+1)
               if flag:
#                  print flag
                  return True
          else:
              break
    return False 



while True:
  try:
    t = input()
    for i in range(t):
        m,n = [int(j) for j in raw_input().split()]
        grid = []
        trip = []
#        grid = [[0 for j in range(m)] for k in range(n)]
        for j in range(m):
            grid.append([int(k) for k in raw_input().split()])
#        print grid
        step = 0
        while True:
            s = raw_input().split()
            if s == ['0','0']:
                break
            else:
                trip.append(s)
                step += 1
#        print step
        res = 0
        
        for x in range(m):
            for y in range(n):                
              flag = False
              DFS(x,y,0)
              if flag:
                res += 1
        print res
  except:
    break
