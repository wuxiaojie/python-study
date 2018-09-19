FINAL = [2001,11,4]
Month_Day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
IsWin = [[[-1 for i in range(32)] for j in range(13)] for k in range(102) ]

def juge(y,m,d):
    pass




while True:
  try:
    T = input()
    for i in range(T):
        date = [int(i) for i in raw_input().split()]
        m,d = date[1:]
        if m == 2 and d == 28:
            print "YES"
            continue 
        elif m == 9 and d == 30:
            print "YES"
            continue 
        elif m == 11 and d == 30:
            print "YES"
            continue 
        elif (m+d)%2 == 0:
            print "YES"
            continue 
        print "NO"
  except:
    break    



