def get_add(m,n,arr,index, cur):
   if index < n:
      if arr[index] == m:
         tmp_cur = [item for item in cur]
         cur.append(m)
         if cur not in res:
            res.append(cur)
         del cur
         for i in range(index+1,n):
             if arr[i] < m:
                tmp = [item for item in tmp_cur]
                tmp.append(arr[i])
                get_add(m-arr[i],n,arr,i+1, tmp)
                del tmp
         del tmp_cur
      elif arr[index] > m:
                get_add(m,n,arr,index+1, cur)        
      else:         
         for i in range(index,n):
             tmp = [item for item in cur]
             tmp.append(arr[i])
             get_add(m-arr[i],n,arr,i+1,tmp) 
             del tmp       
   return None


while True:
  try: 
    nums = [int(i) for i in raw_input().split()]
    t = nums[0]
    n = nums[1]
    if n > 0:
      res = []
      cur = []
      get_add(t,n+2,nums,2,cur)
      print "Sums of %d:" %t 
      if len(res) > 0:
         for item in res:
            out = "+".join([str(i) for i in item])
            print out
      else:
         print "NONE"
    else:
      break
  except:
       break 
      
