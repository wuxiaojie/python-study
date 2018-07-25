import sys


allow_len = [2,5,8,11,14]

def is_all_three(l,lenth):
    s = l[0]
    if l[1] == s and l[2] == s:
       if lenth == 3:
           return True
       else:
           tmp = l[3:]
           return is_all_three(tmp, lenth-3) 
                  
    if s+1 in l and s+2 in l:
       if lenth == 3:
           return True
       else:
           tmp = [i for i in l]
           tmp.remove(s)
           tmp.remove(s+1)
           tmp.remove(s+2)
           return is_all_three(tmp, lenth-3) 


    return False





while True:
     res = False
     seq = raw_input()
     l = [int(i) for i in seq]
     lenth = len(l)
     if lenth in allow_len:
        l.sort()
        p = l[0]
        for i in range(1,lenth):
            if l[i]== p:                  
               tmp = [i for i in l]
               tmp.remove(p)
               tmp.remove(p)
               if len(tmp) == 0:
                  res = True
                  break
               else:
                   res = is_all_three(tmp, lenth-2)
                   if res:
                      break
               continue
            else:
               p = l[i]
            
               
    

    
     if res:
        print 'yes'
     else:
        print 'no'
