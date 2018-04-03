#Find And Replace
words = "It's thanksgiving day. It's my birthday,too!"

print words.find('day')

print words.replace('day', 'month')

#Min and Max
x = [2,54,-2,7,12,98]
#for maxNum in x: 
print "The minimum number in x is ", min(x)
print "The maximum number in x is ", max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]

print x[0]
print x[-1]


#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
a = x[0:5]
b = x[5:11]
newArray = []
newArray.append(a)
print newArray
for i in range(0,len(b)):
	newArray.append(b[i])
print newArray



# x.split()
# print x

# fro, _future_import division - moves to version 3