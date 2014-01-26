unmutatedDNA = ["A", "G", "C", "T", "C"]
mutatedDNA_list = []
mutatedDNA = []

def mutate(unmutatedDNA, index, mutatedDNA, mutatedDNA_list):
	if unmutatedDNA[index] == "A":
		for i in ["C", "G", "T"]:
			saveDNA = unmutatedDNA
			#print "saveDNA", saveDNA
			unmutatedDNA[index] = i

			mutatedDNA = unmutatedDNA
			print "mutated string" , mutatedDNA
			mutatedDNA_list.append(mutatedDNA[:])
			print "the list",  mutatedDNA_list

			unmutatedDNA[index] = "A"
			#print "unmutated" , unmutatedDNA
	elif unmutatedDNA[index] == "C":
		for i in ["A", "G", "T"]:
			saveDNA = unmutatedDNA
			#print "saveDNA", saveDNA
			unmutatedDNA[index] = i

			mutatedDNA = unmutatedDNA
			print "mutated DNA" , mutatedDNA
			mutatedDNA_list.append(mutatedDNA[:])
			unmutatedDNA[index] = "C"
			#print "unmutated" , unmutatedDNA
	elif unmutatedDNA[index] == "G":
		for i in ["C", "A", "T"]:
			saveDNA = unmutatedDNA
			#print "saveDNA", saveDNA
			unmutatedDNA[index] = i

			mutatedDNA = unmutatedDNA
			print "mutated string" , mutatedDNA
			mutatedDNA_list.append(mutatedDNA[:])
			unmutatedDNA[index] = "G"
			#print "unmutated" , unmutatedDNA
	elif unmutatedDNA[index] == "T":
		for i in ["C", "G", "A"]:
			saveDNA = unmutatedDNA
			#print "saveDNA", saveDNA
			unmutatedDNA[index] = i

			mutatedDNA = unmutatedDNA
			print "mutated string" , mutatedDNA
			mutatedDNA_list.append(mutatedDNA[:]) 
			unmutatedDNA[index] = "T"
			#print "unmutated" , unmutatedDNA
	print "mutated DNA list is: " , mutatedDNA_list
	return mutatedDNA_list
for n in range(3):
	mutate(unmutatedDNA, n, mutatedDNA, mutatedDNA_list)
print mutatedDNA_list

print "this is the final list of DNA strings"
#for l in mutatedDNA_list:
#	"".join(l)
#	print l
#print mutatedDNA_list


 #someone on stack overflow said a solution would be to not use 
 #a global variable, but I am using only locally passed ones for this.
 # # http://stackoverflow.com/questions/5280799/list-append-changing-all-elements-to-the-appended-item 
	