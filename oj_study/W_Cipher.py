def right_rotation(n,arr):
    l  = len(arr)
    if l > 0:
      n = n % l
      arr[:l-n] = reversed(arr[:l-n])
      arr[l-n:] = reversed(arr[l-n:])
      arr.reverse()



while True:
  try:
    keys = [int(i) for i in raw_input().split()]
    if keys != [0,0,0]:
       str1 = []
       loc1 = []
       str2 = []
       loc2 = []
       str3 = []
       loc3 = []
       l = 0
       for item in raw_input():
           if item<= 'i' and item >= 'a':
               str1.append(item)
               loc1.append(l)
           elif item<= 'r' and item >= 'j':
               str2.append(item)
               loc2.append(l) 
           else:
               str3.append(item)
               loc3.append(l)  
           l += 1

       right_rotation(keys[0],str1)
       right_rotation(keys[1],str2)
       right_rotation(keys[2],str3)
       res = [''] * l 
       index = 0
       for item in str1:
           res[loc1[index]] = item
           index += 1

       index = 0
       for item in str2:
           res[loc2[index]] = item
           index += 1
 
       index = 0
       for item in str3:
           res[loc3[index]] = item
           index += 1

       print ''.join(res)

    else:
        break
  except:
  	break
