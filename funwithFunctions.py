#Odd/Even
def oddEven():
	for i in range(1, 2000):
		if i % 2 == 0:
			print "Number is i.  This is an even number."
		else:
			print "Number is i.  This is an odd number."
oddEven()

#Multiply:

def multiply(a, b):
	for i in range(0,len(a)):
		a[i] *= b  
	print a

multiply([2,4,10,16], 5)


#Hacker Challenge:



def multiplier(list, num):
	x = []
	for i in range(len(list)): 
		list2= [list[i]*num*"1"]
		x.append(list2)
	print x
multiplier([2,4,8],3)



#type((multiply([2,4,5],3)))
# def multiply(a, b):
# 	for i in range(0,len(a)):
# 		a[i] *= b  
# 	print a
# 	for x in a:
# 		print  a[x]


# def layered_multiples(arr):
# 	multiply([2,4,10,16], 5)
	
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output


