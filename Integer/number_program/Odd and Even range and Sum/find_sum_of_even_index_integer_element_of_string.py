S = '45au875'
res = 0
for ind in range(len(S)):
        if ind % 2 == 0 and '0' <= S[ind] <= '9':  # if S[ind] in '02468':  ONLY TO MATCH THE INDEX POSITION
               res += int(S[ind])
print(res)