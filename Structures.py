#STRUCTURES
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

J = input("Enter a sentence here: ").split()
P = [(len(PAO), PAO) for PAO in J]
print "\nEach word with its corresponding no. of letters:"
print "\t",P
print "Sorted words according to its size:"
print "\t",sorted(P),"\n"

print ' '.join([word for (count, word) in P])