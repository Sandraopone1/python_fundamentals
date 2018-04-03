

def coinTosses():
	countHead = 0
	countTail = 0
	for i in range(1, 5001):
		import random
		randomNum = random.randint(1,2)
		if i == 5000:
			print "Attempt #", i, "Throwing a coin... It's a head! ...", "Got ", countHead, " heads so far", "and ", countTail, " tail so far, Ending the program, thank you!"
		if randomNum == 1 and i < 5000:
			countHead =  countHead + 1
	 		print "Attempt #", i, "Throwing a coin... It's a head! ...", "Got ", countHead, " heads so far", "and ", countTail, " tail so far"
	 	
	 	if randomNum == 2 and i < 5000:
			countTail = countTail + 1
	 		print "Attempt #", i, "Throwing a coin... It's a tail! ...", "Got ", countHead, " heads so far", "and ", countTail, " tail so far"
	 		
	 	# if randomNum <= 79:
		
	 	# 	print "score: ", randomNum, "Your grade is C"
	 	# if randomNum <= 89:
		
	 	# 	print "score: ", randomNum, "Your grade is B"
	 	# if randomNum <= 100:
		
	 	# 	print "score: ", randomNum, "; Your grade is A"
	 		
	 		#Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far

coinTosses()
