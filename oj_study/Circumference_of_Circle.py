pi = 3.141592653589793

def get_len(p1,p2):
    return (abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2) ** 0.5

def get_circumference(a,b,c):	
    r = (a + b + c) / 2
    s = (r - a) * (r -b) * (r - c) * r  
    return 2 * pi * (a * b * c )/ (4 * s ** 0.5)

while True:
  try:
    raw = [float(i) for i in raw_input().split() ]
    p = [[0.0 for i in range(2)] for i in range(3)]
    i = 0
    for item in raw:
        p[i/2][i%2] = item
        i +=1 

    a = get_len(p[0],p[1])
    b = get_len(p[0],p[2])
    c = get_len(p[1],p[2])

    res = get_circumference(a,b,c)
    print "%.2f" %res
  except:
    break
