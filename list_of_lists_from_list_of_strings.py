list_DNA_list_strings=["TCTGAGCTTGCGTTATTTTTAGACC", "GTTTGACGGGAACCCGACGCCTATA", "TTTTAGATTTCCTCAGTCCACTATA", "CTTACAATTTCGTTATTTATCTAAT", "CAGTAGGAATAGCCACTTTGTTGTA", "AAATCCATTAAGGAAAGACGACCGT"]


def listoflistsfromlistofstrings(list_DNA_list_strings):
	templist = []
	for string_1 in list_DNA_list_strings:
		list_1 = []
		for element in string_1:
			list_1.append(element)
		templist.append(list_1)
	list_DNA_list_strings = templist
	return list_DNA_list_strings

print listoflistsfromlistofstrings(list_DNA_list_strings)