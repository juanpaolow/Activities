#MIDTERM
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

def MATCH(words):
    J = 0

    for PAO in words:
        if len(PAO)>1 and PAO[0]==PAO[-1]:
            J+=1
    return J

P=input("ENTER STRING:")
print MATCH(P)

def FRONT(words):
    S=[]
    B=[]

    for word in words:
        if word.startswith('x'):
            S.append(word)
        else:
            B.append(word)

    return sorted(S)+sorted(B)

P=input("ENTER STRING:")
print FRONT(P)