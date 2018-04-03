#Multiples

#Write code that prints all the odd numbers from 1 to 1000.
for i in range(1, 1001, 2):
        print i

#Create another program that prints all the multiples of 5 from 5 to 1,000,000.
for i in range(5, 1000001, 5):
        print i

#Sum List
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
newSum = 0;
a = [1, 2, 5, 10, 255, 3]
for i in a:
	newSum += i
print newSum

#Average List
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

newSum = 0;
a = [1, 2, 5, 10, 255, 3]
for i in a:
	newSum += i
print float(newSum)/len(a)
 
