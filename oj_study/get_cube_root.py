while True:
     try:
       num = int(raw_input())
       r = float(num) 
       l = float(0)
       res = r
       while r - l > 0.0001:
             mid = ( l + r )/2
             if mid * mid *mid > num:
                r = mid
             elif mid * mid * mid < num:
                l = mid

# mid * mid * mid  will never equal to num in python float
       else:
          res = mid
       
       print "%.1f" %res
     except:
         break
