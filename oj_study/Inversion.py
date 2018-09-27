def get_inversion(permutation,N):
    inversion = [0] * N
    for i in range(1,N+1):
        for item in permutation:
            if item == i:
               break
            elif item > i:
               inversion[i-1] +=1
    return inversion


def get_permutation(inversion,N):
    permutation = [0] * N
    for i in range(1,N+1):
        j = 0
        step = inversion[i-1]
        while step > 0:
            if permutation[j] < i and permutation[j] != 0:
               pass
            elif permutation[j] < i:
               step -= 1
            j+= 1
        if permutation[j] > 0:            
           while True:
                  if permutation[j] == 0:
                        permutation[j] = i
                        break
                  else:
                        j += 1
        else:
            permutation[j] = i
    return permutation



while True:
  try:
    N = input()
    if N != 0:     
       raw = raw_input().split()
       flag = raw[0]
       arr = [int(i) for i in raw[1:] ]
       if flag == 'P':
          print ' '.join(str(item) for item in get_inversion(arr,N))
       elif flag == 'I':
             print ' '.join(str(item) for item in get_permutation(arr,N))
        
    else:
       break   
  except:
     break
