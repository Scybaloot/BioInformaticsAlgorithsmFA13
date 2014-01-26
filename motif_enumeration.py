#motif Enumeration
k = 5
d = 2
mutatedDNA = []
list_DNA_list_strings = ["TCTGAGCTTGCGTTATTTTTAGACC", "GTTTGACGGGAACCCGACGCCTATA", "TTTTAGATTTCCTCAGTCCACTATA", "CTTACAATTTCGTTATTTATCTAAT", "CAGTAGGAATAGCCACTTTGTTGTA", "AAATCCATTAAGGAAAGACGACCGT"]
mutated_kmers = []

#Make a list of lists
def listoflistsfromlistofstrings(list_DNA_list_strings):
	templist = []
	for string_1 in list_DNA_list_strings:
		list_1 = []
		for element in string_1:
			list_1.append(element)
		templist.append(list_1)
	list_DNA_list_strings = templist
	return list_DNA_list_strings

list_DNA_list_strings = listoflistsfromlistofstrings(list_DNA_list_strings)
#Find Mutations
def mutate(unmutatedDNA, index, mutatedDNA, mutatedDNA_list, count):
	templist = []
	if count == d or index >= len(unmutatedDNA):
		return	
	else:
		count += 1
		for i in ["A", "C", "G", "T"]:
			saveDNA = unmutatedDNA
			k = unmutatedDNA[index]
			#print "saveDNA", saveDNA
			#print "unmutatedDNA is ", type(unmutatedDNA)
			unmutatedDNA[index] = i
			mutatedDNA = unmutatedDNA
			#print "mutated string" , mutatedDNA
			if mutatedDNA not in mutatedDNA_list:
				mutatedDNA_list.append(mutatedDNA[:])
			templist.append(mutatedDNA[:])
			mutate(mutatedDNA,  index+1 , mutatedDNA, mutatedDNA_list, count)
			#print "the list",  mutatedDNA_list
			unmutatedDNA[index] = k
				#print "unmutated" , unmutatedDNA
		#print "mutated DNA list is: " , mutatedDNA_list
		#print unmutatedDNA, "\n", templist
		return mutatedDNA_list

def create_mutations(unmutatedDNA, mutatedDNA_list, mutatedDNA, d, count):
	for n in range(len(unmutatedDNA)):
		mutate(unmutatedDNA, n, mutatedDNA, mutatedDNA_list, count)
	#print mutatedDNA_list
	#rint len(mutatedDNA_list)
	#print "this is the final list of DNA strings"
	return mutatedDNA_list


for list in list_DNA_list_strings:  #look through each DNA string to create mutated Kmers
	mutatedDNA_list = []
	count = 0
	create_mutations(list, mutatedDNA_list, mutatedDNA, d, count)
	mutated_kmers.append(mutatedDNA_list)

#look for matches of Kmers and their mutated versions

#print "list_of_possible_kmers =" , mutated_kmers
for 

list_of_possible_kmers = mutated_kmers[0]
for i in range(1,len(mutated_kmers)):
	print "length of kmer", len(mutated_kmers)
	templist_kmers = []
	for kmer in list_of_possible_kmers:
		if kmer in list_DNA_list_strings[i]:  #look for matches
			templist_kmers.append(kmer[:])    #if there is a match, add to list
		else:
			pass
	list_of_possible_kmers = templist_kmers


print "list_of_possible_kmers =" , list_of_possible_kmers
# Make the list of list of possible kmers into list of list_DNA_list_stringsfor l in range(len(mutatedDNA_list)):
def makelistofstrings(mutatedDNA_list):
	for l in range(len(mutatedDNA_list)):
		newstring = "".join(mutatedDNA_list[l])
		mutatedDNA_list.pop(l)
		mutatedDNA_list.insert(l, newstring)
		#print mutatedDNA_list
	print mutatedDNA_list

print makelistofstrings(list_of_possible_kmers)