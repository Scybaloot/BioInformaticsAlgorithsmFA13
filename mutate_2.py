unmutatedDNA = ["A", "G"]
mutatedDNA_list = []
mutatedDNA = []
d = 2
count = 0

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
		print unmutatedDNA, "\n", templist
		return mutatedDNA_list

def create_mutations(unmutatedDNA, mutatedDNA_list, mutatedDNA, d, count):
	for n in range(len(unmutatedDNA)):
		mutate(unmutatedDNA, n, mutatedDNA, mutatedDNA_list, count)
	#print mutatedDNA_list
	print len(mutatedDNA_list)
	print "this is the final list of DNA strings"
	return mutatedDNA_list

create_mutations(unmutatedDNA, mutatedDNA_list, mutatedDNA, d, count)


for l in range(len(mutatedDNA_list)):
	newstring = "".join(mutatedDNA_list[l])
	mutatedDNA_list.pop(l)
	mutatedDNA_list.insert(l, newstring)
	#print mutatedDNA_list
print mutatedDNA_list


 #someone on stack overflow said a solution would be to not use 
 #a global variable, but I am using only locally passed ones for this.
 # # http://stackoverflow.com/questions/5280799/list-append-changing-all-elements-to-the-appended-item 
	