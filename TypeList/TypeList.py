def listType(x):
    sum = 0
    newString = ""
    strings = 0
    numbers = 0
    for element in x:
        if isinstance(element,int):
            sum = sum + element
            numbers = numbers + 1
        if isinstance(element,str):
            count = count + 1
            newString = newString + " " + element
	if strings > 0 and numbers > 0:
        print "The list you entered is of mixed type"
        print "String: " + newString
        print "Sum: " + str(sum)
    elif count > 0 and numbers < 1:
        print "The list you entered is of string type"
        print "String: " + " ".join(x)
    else:
        print "The list you entered is of integer type" 
        print "Sum: " + sum
    
    listType(['magical unicorns',19,'hello',98.98,'world']):