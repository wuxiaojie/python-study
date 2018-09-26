def Is_Reachable(n,arr):
    if n % 2 == 1:
       return True
    else:
        odd = 0
        even = 0
        for k in range(n):
            if arr[k] == 1:
               if k % 2 == 1:
                     odd += 1
               else:
                     even += 1
        # print 'odd:%d, even:%d, abs(odd-even):%d' %(odd,even,abs(odd-even))
        # print abs(odd - even)
        if abs(odd - even) <= 1:
            return True
        else:
            return False



while True:
  try:
    T = input()
    for i in range(T):
        raw = [int(j) for j in raw_input().split()]
    
        if Is_Reachable(raw[0],raw[1:]):
            print "YES"
        else:
            print "NO"
  except:
    break

