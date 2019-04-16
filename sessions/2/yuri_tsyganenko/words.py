rus_dict = open("dict.txt").readlines()

for w in rus_dict:
	for n in range(1,len(w)-1):
		wnew = w[n:] + w[:n]		
		if wnew in rus_dict:
			print(wnew)

