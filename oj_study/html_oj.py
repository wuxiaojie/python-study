import sys
len1=0
for line in sys.stdin:
  list1 = line.split()
  for w in list1:
    if w == '<br>':
      print
      len1 = 0;
    elif w == '<hr>':
      if len1 !=0:
        print
      print '-'*80
      len1 = 0;
    else:
      if len1+len(w)>80:
        print
        print w,
        len1 = 0;
      else:
        print w,
      len1 += len(w)+1
    
