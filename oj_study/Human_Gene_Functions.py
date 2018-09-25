
SCORES={'AA':5,'AC':-1,"CC":5,'AG':-2,'CG':-3,'GG':5,'AT':-1,'CT':-2,'GT':-2,"TT":5,'-A':-3,'-C':-4,'-G':-2,'-T':-1}

# def complex_similarity(str1,str2,l1,l2):
#     sim = 0
#     if l1 == 0 or l2 == 0:
#        if l1 == 0:
#           ts = str2
#        else:
#           ts = str1
#        for item in ts:
#           sim += SCORES['-' + item] 
#        return sim
#     else:
#        return max(SCORES[''.join(sorted(str1[0]+str2[0]))] + similarity(str1[1:],str2[1:],l1-1,l2-1), \
#         SCORES['-' + str1[0]] + similarity(str1[1:],str2,l1-1,l2), SCORES['-' + str2[0]] + similarity(str1,str2[1:],l1,l2-1)) 





while True:
  try:
    T = input()
    for i in range(T):
        l1,str1 = raw_input().split()
        l2,str2 = raw_input().split()
        l1 = int(l1)
        l2 = int(l2)
#        sim = similarity(str1,str2,l1,l2)
        dp = [ [0 for j in range(l2+1)]  for k in range(l1+1)]
        for j in range(1,l2+1):
        	dp[0][j] = dp[0][j-1] + SCORES['-' + str2[j-1]]
        for j in range(1,l1+1):
        	dp[j][0] = dp[j-1][0] + SCORES['-' + str1[j-1]]        	
        for j in range(1,l1+1):
            for k in range(1,l2+1):
                dp[j][k] = max(dp[j-1][k] + SCORES['-' + str1[j-1]], dp[j][k-1] + SCORES['-' + str2[k-1]], dp[j-1][k-1]+ SCORES[''.join(sorted(str1[j-1]+str2[k-1]))])

        print dp[l1][l2]
        del dp
  except:
    break


