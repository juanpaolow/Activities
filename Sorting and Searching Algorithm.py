#SORTING AND SEARCHING ALGORITHM
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

def bubblesort(nlist):
    for NUM in range(len(nlist)-1,0,-1):
        for P in range(NUM):
            if nlist[P]>nlist[P+1]:
                J = nlist[P]
                nlist[P] = nlist[P+1]
                nlist[P+1] = J

def binary_search(arr,val):
    if len(arr) == 0 or (len(arr)==1 and arr[0]!=val):
        print "\n",val, "NO PRIME NUMBER DETECTED"
        return False

    PAO = arr[len(arr)/2]
    if val == PAO:
        print "\n",val,"PRIME NUMBER DETECTED"
        return True
    if val < PAO: return binary_search(arr[:len(arr)/2],val)
    if val > PAO: return binary_search(arr[len(arr)/2+1:],val)

if __name__ == "__main__":
    def prime():
        nlist = [2,5,7,11,3,23,17,19,13,37,43,31,29,47,41,53,67,61,59,97,83,73,71,89,83,79]
        bubblesort(nlist)

        print "\nDISCOVER THE NUMBER ENTERED IS A PRIME NUMBER OR NOT"

        x = input("ENTER A NUMBER: ")

        print binary_search(nlist,x)
        return prime()
    prime()