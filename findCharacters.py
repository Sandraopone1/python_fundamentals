
# def findCharacters(listed,singlechar):
# 	newArr = []
# 	for x in range(0,len(listed)):
# 		if listed[x].find(singlechar) != -1:
# 			newArr.append(listed[x])
# 	return newArr
# print findCharacters(['hello', 'the'], 'l')


word_list = []
def FindCharacters(list, character ):
    for word in list:
        for char in word:
            if char == character :
                word_list.append(word)
                break
            else:
                pass
    print word_list 

FindCharacters(['hello','world','my','name','is','Anna'], "o" )