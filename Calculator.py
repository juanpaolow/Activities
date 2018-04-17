#CALCULATOR
#BANGAYAN, JUAN PAOLO S.
#GITHUB.COM/JUANPAOLOW
#JUANPAOLOBANGAYAN@YAHOO.COM

while True:
	print("1. ADD (+)")
	print("2. SUBTRACT (-) ")
	print("3. MULTIPLY (*)")
	print("4. DIVIDE (/) ")
	print("5. EXIT")
	PAO=int(input("SELECT AN OPTION:"))
	if (PAO>=1 and PAO<=4):
		print("ENTER TWO NUMBERS:")
		A=int(input())
		B=int(input())
		if PAO == 1:
			ANS = A+B
			print("SUM IS =", ANS)
		elif PAO == 2:
			ANS = A-B
			print("DIFFERENCE IS =", ANS)
		elif PAO == 3:
			ANS = A*B
			print("PRODUCT IS =",ANS)
		else:
			ANS = A/B
			print("QUOTIENT IS =",ANS)
	elif PAO ==5:
		break
	else:
		print("Wrong input!")