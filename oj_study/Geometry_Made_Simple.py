import sys

def get_rec(a,c):
    if a < c:
        return float((c ** 2 - a ** 2) ** 0.5)
    else:
        return -1
            
def get_hypo(a,b):
    return float((a ** 2 + b ** 2) ** 0.5)

def get_neg(line_list):
    index = line_list.index('-1')
    if index == 2:
       return index,get_hypo(float(line_list[0]),float(line_list[1]))
    else:
      return index,get_rec(float(line_list[1-index]),float(line_list[2]))       

end_list = ["0","0","0"]
index_list = ['a','b','c']
count = 0

while True:
        count += 1
        line_list = sys.stdin.readline().strip().split()
        if line_list == end_list:
            break
        else:
            index, lenth = get_neg(line_list)
            print "Triangle #%d" %count
            if lenth == -1:
                print "Impossible.\n"
            else:
                print "%s = %.3f\n" %(index_list[index],lenth)
        
