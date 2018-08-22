steps=['fill A', 'fill B', 'empty A', 'empty B','pour A B', 'pour B A', 'success']

def jugs(a,b,suc):
    
    if b == N:
       suc.append(steps[6])
       all.append(suc)
#       print a,b
    else:
        if a == A:
           if b == B:
              if (0,B) not in state:
#                 state = [i for i in sta]
                 state.append((0,B))
                 tmp = [i for i in suc]
                 tmp.append(steps[2])
                 jugs(0,B,tmp)
                 del tmp
#                 del state


           elif b == 0:
               if (0,A) not in state:
                    state.append((0,A))
                    tmp = [i for i in suc]
                    tmp.append(steps[4])
                    jugs(0,A,tmp)
                    del tmp
               if (A,B) not in state:
                    state.append((A,B))
                    tmp = [i for i in suc]
                    tmp.append(steps[1])
                    jugs(A,B,tmp)
                    del tmp

           else:
               if(0,b) not in state:
                    state.append((0,b))
                    tmp = [i for i in suc]
                    tmp.append(steps[2])
                    jugs(0,b,tmp)
                    del tmp 
               if a+b <= B:
                  if (0,a+b) not in state:
                    state.append((0,a+b))
                    tmp = [i for i in suc]
                    tmp.append(steps[4])
                    jugs(0,a+b,tmp)
                    del tmp 
               else:
                  if (a-(B-b),B) not in state:
                     state.append((a-(B-b),B))
                     tmp = [i for i in suc]
                     tmp.append(steps[4])
                     jugs(a-(B-b),B,tmp) 
                     del tmp 
        elif a == 0:
           if b == B:
              if (A,B) not in state:
                 state.append((A,B))
                 tmp = [i for i in suc]
                 tmp.append(steps[0])
                 jugs(A,B,tmp)
                 del tmp
              if (A, B-A) not in state:
                 state.append((A,B-A))
                 tmp = [i for i in suc]
                 tmp.append(steps[5])
                 jugs(A,B-A,tmp)
                 del tmp  
           elif b == 0:
               if (0,B) not in state:
                    state.append((0,B))
                    tmp = [i for i in suc]
                    tmp.append(steps[1])
                    jugs(0,B,tmp)
                    del tmp 
               if (A,0) not in state:
                    state.append((A,0))
                    tmp = [i for i in suc]
                    tmp.append(steps[0])
                    jugs(A,0,tmp)
                    del tmp
           else:
               if (A,b) not in state:
                     state.append((A,b))
                     tmp = [i for i in suc]
                     tmp.append(steps[0])
                     jugs(A,b,tmp)
                     del tmp
               
               if b>=A:
                      if (A,b-A) not in state: 
                         state.append((A,b-A))
                         tmp = [i for i in suc]
                         tmp.append(steps[5])
                         jugs(A,b-A,tmp)
                         del tmp
               elif (b,0) not in state:
                         state.append((b,0))
                         tmp = [i for i in suc]
                         tmp.append(steps[5])
                         jugs(b,0,tmp)
                         del tmp

        
        else:
           if b == B:
                 if (A,B-(A-a)) not in state:
                       state.append((A,B-(A-a)))                 	
                       tmp = [i for i in suc]
                       tmp.append(steps[5])
                       jugs(A,B-(A-a),tmp)
                       del tmp
                 if (a,0) not in state:
                       state.append((a,0))                 	
                       tmp = [i for i in suc]
                       tmp.append(steps[3])
                       jugs(a,0,tmp)
                       del tmp
           elif b == 0:
               if (a,B) not in state:
               	    state.append((a,B))
                    tmp = [i for i in suc]
                    tmp.append(steps[1])
                    jugs(a,B,tmp)
                    del tmp
               if (0,a) not in state:
                    state.append((0,a))               	
                    tmp = [i for i in suc]
                    tmp.append(steps[4])
                    jugs(0,a,tmp)
                    del tmp
           else:
               if (a,0) not in state:
                       state.append((a,0))
                       tmp = [i for i in suc]
                       tmp.append(steps[3])
                       jugs(a,0,tmp)
                       del tmp
               if (0,b) not in state:
               	       state.append((0,b))
                       tmp = [i for i in suc]
                       tmp.append(steps[2]) 
                       jugs(0,b,tmp)
                       del tmp

               if a+b <= B:
                  if (0,a+b) not in state:
                       state.append((0,a+b))
                       tmp = [i for i in suc]
                       tmp.append(steps[4])
                       jugs(0,a+b,tmp) 
                       del tmp 
               else:
                     if (a-(B-b),B) not in state:
                       state.append((a-(B-b),B))
                       tmp = [i for i in suc]
                       tmp.append(steps[4])
                       jugs(a-(B-b),B,tmp)
                       del tmp 

               if a+b <=A:
                       if(a+b,0) not in state:
                       	 state.append((a+b,0))
                         tmp = [i for i in suc]
                         tmp.append(steps[5])                         
                         jugs(a+b,0,tmp)
                         del tmp
               else:
                     if (A,b-(A-b)) not in state:
                     	state.append((A,b-(A-b)))
                        tmp = [i for i in suc]
                        tmp.append(steps[5])
                        jugs(A,b-(A-b),tmp) 
                        del tmp


while True:
  try:
    nums = [int(i) for i in raw_input().split() ]
    A = nums[0]
    B = nums[1]
    N = nums[2]

    s = []
    all = []
    a = 0
    b = 0
    state = [(0,0)]
    jugs(a,b,s)
#    print state
#    print all
    l = len(all)
    if l > 0:
       res = all[0]
       for item in all:
       	   if len(item) < len(res):
       	   	  res = item 
       for item in res:
       	   print item
  except:
     break  


