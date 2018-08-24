N = 6

flag=False

def lotto(nums, s, r,k, res):
    if r > 0:
        dif = k-s-r+1
#        print "dif:%d" %dif
        if dif >0 :
          for i in range(dif+1):
             tmp = [item for item in res]
             tmp.append(nums[s+i])
             lotto(nums, s+i+1,r-1,k,tmp)
             del tmp
        else:
            f = 0 
            for item in res:
                print item,
                f += 1
            for item in nums[s:]:
                print item,
                f += 1
            if f > 0:
                 print
    else: 
          f = 0
          for item in res:
            print item,
            f += 1
          if f > 0:
              print
    

while True:
  try:  
    orin = raw_input()
    if orin == '0':
       flag == False
       break
    else:
        if flag:
          print
        nums = [int(i) for i in orin.split()]
        k = nums[0]
        res = []
        lotto(nums,1,N,k,res)
        flag = True
    

  except:
    break
