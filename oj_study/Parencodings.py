def get_parentheses(P_sequence,n):
    res = [''] * (2 * n)
    pre = 0
    index = 0
    for item in P_sequence:
           for i in range(index,index+item-pre):
                    res[index] = '('
                    index += 1
           res[index] = ')'
           pre = item
           index += 1        
    return res


def get_W_sequence(parentheses):
    res = []
    left  = []
    right = []
    index = 0
    # for item in P_sequence:
    #     if item > pre:
    #        res.append(1)
    #        pre = item 
    #     else:        
    #     index += 1 
            
    for item in parentheses:
        if item == '(':
           left.append([index,0])
        else:
           tmp = 1            
           for l in left[::-1]:
                  if l[1] == 0:
                    for r in right:
                       if r > l[0]:
                          tmp += 1
                         
                    l[1] = 1
                    break
           right.append(index)
           res.append(tmp)
                
        index += 1

    return res


while True:
  try:
    t = input()
    for j in range(t):
        n = input()
        P_sequence = [int(i) for i in raw_input().split()]
        parentheses = get_parentheses(P_sequence,n)
#        print ''.join(parentheses)
        W_sequence = get_W_sequence(parentheses)
        print ' '.join([str(i) for i in W_sequence])

  except:
    break
