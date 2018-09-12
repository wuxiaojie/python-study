while True:
  try:
    raw = raw_input()
    if raw != "0":
       index = 1
       res = 0
       for item in raw[::-1]:
              res += int(item) * (2 ** index - 1)
              index += 1
       print res
    else:
        break
  except:
    break
