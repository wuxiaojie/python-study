
def all_possible(sr_index, oj_index, sr, oj, st, res, lim):
   
    if len(st) == 0:
       if sr_index <= lim:
       	  res_tmp = [i for i in res]
          st_tmp = [i for i in st] 
          st_tmp.append(sr[sr_index])           
          res_tmp.append('i')          
          all_possible(sr_index + 1, oj_index, sr, oj, st_tmp, res_tmp, lim)
          del st_tmp
          del res_tmp 
       else:
             if oj_index == lim+1:
                all.append(' '.join(res))

    else:
        if st[-1] == oj[oj_index]:
           if sr_index <= lim:
              res_tmp2 = [i for i in res]
              st_tmp2 = [i for i in st]
              st_tmp2.append(sr[sr_index])           
              res_tmp2.append('i') 
              all_possible(sr_index+1, oj_index, sr, oj, st_tmp2, res_tmp2, lim)
              del st_tmp2
              del res_tmp2
           res_tmp = [i for i in res]
           st_tmp = [i for i in st] 
           st_tmp.pop()
           res_tmp.append('o')
           all_possible(sr_index, oj_index+1, sr, oj, st_tmp, res_tmp, lim)
           del st_tmp
           del res_tmp
        else:
           if sr_index <= lim:
              res_tmp = [i for i in res]
              st_tmp = [i for i in st] 
              st_tmp.append(sr[sr_index])
              res_tmp.append('i')
              all_possible(sr_index+1, oj_index, sr, oj, st_tmp, res_tmp, lim)
              del st_tmp
              del res_tmp
        


while True:
    try:
      sr = [i for i in raw_input()]
      oj = [j for j in raw_input()]
      lim = len(sr) - 1
#      print lim
      res = []
      st = []
      sr_index = 0
      oj_index = 0
      all = []
      print "["
      all_possible(sr_index, oj_index, sr, oj, st, res, lim)
      all.sort()
      for item in all:
      	  print item+' '
      print "]" 
    except:
      break
