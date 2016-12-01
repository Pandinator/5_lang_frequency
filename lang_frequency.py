path = input() #User inputs a path to a file

word_list = open(path, "r").read().split() #Open the file

lst_sorted=sorted([ss for ss in set(word_list) if len(ss)>0],   #The term in squared brackets returns all unique strings 
                   key=word_list.count,   						#in the list, which are not empty
                   reverse=True)
j = 1
for word in lst_sorted: #print top-10 words
	if j > 10:
		break
	else:
		j += 1
		print(word, end=", ")
