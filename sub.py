match = "PPPP"

def substitute_mer(match):
	match_list = []
	for letter in match:
		match_list.append(letter)
	for y in range(len(match)):
		for letter2 in ["A", "C", "G", "T"]:
			print "letter equals", letter2 
			match_list[y] = letter2
			match_list[y-1] = match[y-1]
			match = "".join(match_list)
			

			print match

substitute_mer(match)