k = 12
outputDNA = "GGCAGTCTGTTGAATTTACGTGATGTTGGCAGTCACGTGATGTTACGTGATGTTTTGCATGAATGTTGAATTTACGTGATGTTTTGCATGAATGTTGAATTTACGTGATGTTTTGCATGAAGGCAGTCACGTGATGTTCTTGGAAGGCAGTCTTGCATGAAACGTGATGTTCTTGGAACTTGGAAACGTGATGTTACGTGATGTTTTGCATGAATGTTGAATTTGGCAGTCTTGCATGAATTGCATGAAGGCAGTCGGCAGTCTTGCATGAATTGCATGAAACGTGATGTTTGTTGAATTTGGCAGTCTTGCATGAATTGCATGAAGGCAGTCGGCAGTCACGTGATGTTACGTGATGTTACGTGATGTTCTTGGAAGGCAGTCACGTGATGTTTTGCATGAATTGCATGAAGGCAGTCTTGCATGAAGGCAGTCCTTGGAATTGCATGAATTGCATGAACTTGGAATGTTGAATTTTTGCATGAAACGTGATGTTCTTGGAAGGCAGTCCTTGGAATGTTGAATTTTTGCATGAAACGTGATGTTGGCAGTCTGTTGAATTTTTGCATGAATTGCATGAAACGTGATGTTTGTTGAATTTTTGCATGAAGGCAGTCTTGCATGAACTTGGAATTGCATGAATGTTGAATTTTGTTGAATTTTTGCATGAACTTGGAAACGTGATGTTTGTTGAATTTTGTTGAATTTTGTTGAATTTCTTGGAAGGCAGTCTTGCATGAATTGCATGAACTTGGAATGTTGAATTTCTTGGAATGTTGAATTTGGCAGTCTTGCATGAAGGCAGTCTGTTGAATTTCTTGGAATTGCATGAAGGCAGTCTTGCATGAATTGCATGAAGGCAGTCTGTTGAATTTGGCAGTCACGTGATGTTGGCAGTCTGTTGAATTTGGCAGTCTGTTGAATTTGGCAGTCTGTTGAATTTTGTTGAATTTACGTGATGTTGGCAGTCACGTGATGTT"

def findK_mers(k, outputDNA):
	dict_kmers = {}
	for i in range(len(outputDNA)):
		#check if string is in dictionary of k-mers
		k_mer_being_looked_at = outputDNA[i:i+k]
		if k_mer_being_looked_at in dict_kmers:
			dict_kmers[k_mer_being_looked_at] += 1
		else:
			dict_kmers[k_mer_being_looked_at] = 1
	print dict_kmers
	return dict_kmers  #outputs a dictionary of the k-mers

dict_kmers = findK_mers(k, outputDNA)


list_most_common_k_mers = []

list_tuple_kmers_occurence = dict_kmers.items()
def findMostFrequent(list_tuple_kmers_occurence):
	occurence_most_Common_K_mer = 0
	for kmer in list_tuple_kmers_occurence:
		if kmer[1] > occurence_most_Common_K_mer:
			print kmer
			#print "more common"
			list_most_common_k_mers = []
			list_most_common_k_mers.append(kmer[0])
			occurence_most_Common_K_mer = kmer[1]
		if kmer[1] == occurence_most_Common_K_mer:
			#print "same common"
			list_most_common_k_mers.append(kmer[0])
		else:
			pass
			#print "not as common"
	return list_most_common_k_mers

print findMostFrequent(list_tuple_kmers_occurence)



