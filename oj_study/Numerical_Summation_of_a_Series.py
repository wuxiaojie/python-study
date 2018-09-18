
x = 0.000
for item in range(2001):
    sum = 0
    for k in range(1,10000):
       sum += (1.0-x) / (k * (k+1) * (k+x))
    sum += (1-x) / (2 * 10000 * 10000) + 1.0
    print "%5.3f %16.12f" %(x,sum)
    x += 0.001

