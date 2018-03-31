#EXERCISE NO. 1 - ARRAYS USING LIST
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

jps=[['T','H','E'], ['Q','U','I','C','K'], ['B','R','O','W','N'], ['F','O','X'],[ 'J','U','M','P','S'], ['O','V','E','R'], ['T','H','E'], ['L','A','Z','Y'], ['D','O','G']]
jps.append(['O','K','A','Y'])
J = [jps[1][3],jps[7][1],jps[2][1],jps[4][3],jps[0][2]]
P = [jps[8][0],jps[1][2],jps[0][2],jps[4][2]]
P.insert(0," ")
S = [":","D"]
S = " ".join(S)
B = ['E','V','E','R','Y','O','N','E',","]
B = " ".join(B)
print B," ".join(J + P)," ",S
#CARPE DIEM = SIEZE THE DAY