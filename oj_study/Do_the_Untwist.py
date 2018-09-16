while True:
  try:
    raw = raw_input()
    if raw != '0':
       k,ciphertext=raw.split()
       k = int(k)
       ciphercode=[]
       n = 0
       for item in ciphertext:
           if item == '_':
                    ciphercode.append(0)
           elif item == '.':
              ciphercode.append(27)
           else:
              ciphercode.append(ord(item)-ord('a')+1)
           n += 1
       res = []
       plaincode = [0] * n

       for i in range(n):
           tmp = ciphercode[i] 
           if tmp + i < 28:
           	     plaincode[(k * i) % n] = tmp + i 
           else:
           	   plaincode[(k * i) % n] = (tmp + i - 28) % 28
               

       for item in plaincode:
           if item  == 0:
              res.append('_')
           elif item == 27:
               res.append('.') 
           else:     
              res.append(chr(item + ord('a') -1 ))

       print ''.join(res)
  
          
    else:
        break
  except:
  	break
