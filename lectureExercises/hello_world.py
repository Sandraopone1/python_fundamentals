"""print "Hello World!"
x = "Hello Python"
print x
y = 42
print y """

"""# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function' """

# name = "Zen"
# print "My name is", name 
# print "My name is " + name 

# age = 20
# print "My age is", age
# print "My age is " + age

first_name = "Zen"
last_name = "Coder"
middle_name = "m"
print "My name is {} {} {}".format(first_name, last_name, middle_name)

hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world
x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"
U = "happy"
print U.count("p")
print U.endswith("p")
print U.endswith("y")
print U.endswith("y")
fruits = ['apple', 'banana', 'orange', 'strwaberry']
vegetables = ['lettuce, cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables
print fruits_and_vegetables
salad = 3 * vegetables
print salad

x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];

my_list = [1, 'Zen', 'hi']
print len(my_list)


"""enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence
list.extend(list2) adds all values from a second sequence to the end of the original sequence.
list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
list.index(value) returns the index position in a list for the given parameter."""
#conditions
age = 15
if age >= 18:
  print 'Legal age'
else:
  print 'You are so young!'

  #loops

  for count in range(0, 5):
      print "looping ", count