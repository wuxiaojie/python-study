while True:
  try:   
    N = int(raw_input())
    arr = [[0 for i in range(N) ] for i in range(N)] 
    sums = [[0 for i in range(N) ] for i in range(N)] 
    index = 0
    while True:
        for item in raw_input().split():
            arr[index/N][index%N] = int(item)
            if index%N == 0:
               sums[index/N][index%N] = arr[index/N][index%N]
            else:
               sums[index/N][index%N] = arr[index/N][index%N] + sums[index/N][index%N-1] 
#            print arr[index/N][index%N]
            index += 1
            if index == N*N:
                break
        if index == N*N:
                break
#    print arr  
#    print sums
    s = 0
    max = -127 
    for i in range(N):
        for j in range(i,N):
            s = 0
            for k in range(N):
                if s<0:
                   s = 0
                if i == 0:
                   s += sums[k][j]
                else:
                   s += sums[k][j] - sums[k][i-1]
                if s > max:
                    max = s
    print max
  except:
    break
