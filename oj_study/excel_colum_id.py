while True:
    try: 
        n = int(raw_input())
        res = []
        while n > 0:
              tmp = (n - 1) % 26
              res.append(tmp)
              n = (n-1)/26
        col_id = ''

        for item in res[::-1]:
            col_id += chr(item + ord("A"))
        print col_id
    except:
        break 
