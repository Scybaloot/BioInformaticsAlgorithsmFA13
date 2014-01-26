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