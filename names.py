students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# count = 1;
# for i in students:
# 	for data in i.values():
# 		if data % 2 == 0:
# 			print data
# 		count =+ 1
# 		 #.values()

for i in students:
    print i["first_name"], i["last_name"]
 



#  for i in students:
#     count = 1
#     a = len(i["first_name"]) + len(i["last_name"])
#     b = i["first_name"], i["last_name"]
#     count+=1
#     print count, b , a