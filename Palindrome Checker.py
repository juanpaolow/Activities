J= "RACECAR"
print J

P = "CAR RACE"
print P


J = J.replace(" ","")
J = J.lower()

P = P.replace(" ","")
P = P.lower()


J_list = list(J)
P_list = list(P)


J_rev = J_list[::-1]
P_rev = P_list[::-1]


if J_rev == J_list:
    print ("\n\n\n PALINDROME DETECTED")
else:
    print ("\n\n\n NO PALINDROME DETECTED")

if P_rev == P_list:
    print ("\n\n\n PALINDROME DETECTED")
else:
    print ("\n\n\n NO PALINDROME DETECTED")