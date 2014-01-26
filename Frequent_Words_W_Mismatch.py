k = 4
d = 1
DNA_String = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
n = len(DNA_String)
dict_matches = {}

#answer supposed to get = GCACACAGAC GCGCACACAC



# Compare pieces to other pieces
def approxPatternMatching(match, d, DNA_String, n, dict_matches, p):
	for l in range(p+1, len(DNA_String)-k+1):

		possible_Match = DNA_String[l:l+k]
		#print "match = " , match
		#print "possible match =" , possible_Match
		error = 0

			#check for mismatches to see if they exceed d 

		for m in range(len(possible_Match)):
			#print m
			if (possible_Match[m] != match[m]): 
				error +=1
			else:
				pass

		if error <= d:
			# print possible_Match
			#if there is a match, add to a dictionary. If already in dictionary, +=1
			if match in dict_matches:
				dict_matches[match] += 1
			else:
				dict_matches[match] = 1
			if possible_Match in dict_matches:
				dict_matches[possible_Match] += 1
			else:
				dict_matches[possible_Match] = 1
		else:
			pass

	return dict_matches
	#string_points = " ".join(list_of_Points_with_Match)
	#print string_points
	#return string_points == output_test

# break DNA_String into pieces


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
			return match

def findMostFrequent(dict_matches):
	list_tuple_kmers_occurence = dict_matches.items()
	occurence_most_Common_K_mer = 0
	for kmer in list_tuple_kmers_occurence:
		print kmer
		if kmer[1] > occurence_most_Common_K_mer:
			#print "more common"
			list_most_common_k_mers = []
			list_most_common_k_mers.append(kmer[0])
			occurence_most_Common_K_mer = kmer[1]
		elif kmer[1] == occurence_most_Common_K_mer:
			#print "same common"
			list_most_common_k_mers.append(kmer[0])
		else:
			pass
			#print "not as common"
	return list_most_common_k_mers

print findMostFrequent(list_tuple_kmers_occurence)


for p in range(len(DNA_String)-k+1):
	match = DNA_String[p:p+k]
	match = substitute_mer(match)
	dict_matches = approxPatternMatching(match, d, DNA_String, n, dict_matches, p)


#look for ones with most matches. 