#stars = *
#Part I
# def draw_stars(listNum):
# 	for i in range(0, len(listNum)):
# 		stars = "*" * listNum[i]
# 		print stars
# draw_stars([4, 6, 1, 3, 5, 7, 25])

#part2
def findCharacters(listed,singlechar):
        newArr = []
    for x in range(0,len(listed)):
        if listed[x].find(singlechar) != -1:
            newArr.append(listed[x])
    return newArr
print findCharacters(['hello', 'the'], 'l')




# def multiplier(list, num):
#     x = []
#     for i in range(len(list)): 
#     list2= [list[i]*num*"1"]
#     x.append(list2)
# print x
# multiplier([2,4,8],3)
