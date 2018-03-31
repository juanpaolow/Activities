#EXERCISE NO. 5 - DICTIONARIES
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

print "ENTER YOUR GRADES HERE"

print "\tGRADING SYSTEM\n\t"
J = input("\tTESTS: ")
P = input("\tEXERCISES: ")
S = input("\tATTENDANCE: ")
JUAN = {}


def Grades():
    NAME = input("\nNAME:")

    A = input("     Enter Quizzes here: ")
    S = input("     Enter Exercises here: ")
    C = input("     Enter Attendance here: ")
    B = {"Quiz": list(A), "exercise": list(S), "Attendance": list(C), "FINAL GRADE": []}

    B["Quiz"] = float(sum(a) / len(a))
    B["exercise"] = float(sum(b) / len(b))
    B["FINAL GRADE"] = B["Quiz"] * J + B["exercise"] * P + B["Attendance"] * S
    PAO = B["FINAL GRADE"]
    print "     FINAL GRADE: ", B["FINAL GRADE"]
    if B["FINAL GRADE"] >= 75:
        print "     CONGRATULATIONS ", NAME, ",YOU'VE PASSED THE SUBJECT"
    elif B["FINAL GRADE"] <= 74:
        print "\tI'M SORRY", NAME, ",YOU'VE FAILED"
    JUAN[NAME] = PAO

    x = input("\n[1] Continue... [2] Print Result     : ")
    if x == 1:
        return Grades()
    elif x == 2:
        print JUAN

print Grades()