
while True:
  try:

    N = int(raw_input())
    exons = []
    for i in range(N):
        ex = [int(j) for j in raw_input().split() ]
        ex.append(i+1)
        exons.append(ex)
        exons.sort()
#    print exons

    left = [[i+1] for i in range(N)]
    right = [[i+1] for i in range(N)]

    for i in range(N):
        for j in range(0,i):
              if exons[i][0] > exons[j][1] and len(left[j])+1 > len(left[i]):
                 left[i].append(j+1) 


#    print left

    for i in range(N-1,-1,-1):
           for j in range(N-1,i,-1):
                  if exons[j][0] > exons[i][1] and len(right[j])+1 > len(right[i]):
                     right[i].append(j+1)


#    print right 
    max_len = 0
    res = 0
    for i in range(N):
        l = len(left[i])
        r = len(left[i])
        if l+r-1 > max_len:
            res = i 
            left[i].extend(right[i][1:])
            max_len = l+r-1

    left[res].sort()
#    print left[res]
    for item in left[res]:
        print exons[item-1][2],
    print 
  except:
  	break

           
