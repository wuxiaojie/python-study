import sys

while True:
  try:
    N, M = [int(num) for num in sys.stdin.readline().strip().split() ]
    scores = [int(num) for num in sys.stdin.readline().strip().split() ][0:N]
    res = []
    i = 0
    while(i < M):
      query = sys.stdin.readline().strip().split()[0:3]
      if query[0] == 'Q':
        if int(query[1]) <= int(query[2]):
           res.append(max(scores[int(query[1])-1:int(query[2])]))
    #       print max(scores[int(query[1])-1:int(query[2])])
        else:
    #        print max(scores[int(query[2])-1:int(query[1])])
            res.append(max(scores[int(query[2])-1:int(query[1])]))
      elif query[0] == 'U':
           scores[int(query[1])-1] = int(query[2])
    #       res.append(max(scores))
    #       print max(scores)
      i += 1
    for item in res:
        print (item)
  except ValueError:
        break
