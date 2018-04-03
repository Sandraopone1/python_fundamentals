def filter(si):
	if type(si) == str:
		if len(si) >= 50:
			 print "Long sentence"
		else:
			print "Short sentence"
	if type(si) == int:
		if si >= 100:
			 print "That's a big number!"
		else:
			print "That's a small number"

	if type(si) == list:
		if len(si) >= 10:
			 print "Big list!"
		else:
			print "short list"
filter("Rubber baby buggy bumpers")


def filterByType(x):
    if isinstance(x,int):
        if x < 100:
            print "That's a small number"
        else:
            print "That's a big number!"
    if isinstance(x,str):
        if len(x) < 50:
            print "That's a short sentence"
        else:
            print "That's a long sentence!"
    if isinstance(x,list):
        if len(x) < 10:
            print "That's a short list"
        else:
            print "That's a long list!"
filterByType([])