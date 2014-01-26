string_Codons_aminos = "AAA K AAC N AAG K AAU N ACA T ACC T ACG T ACU T AGA R AGC S AGG R AGU S AUA I AUC I AUG M AUU I CAA Q CAC H CAG Q CAU H CCA P CCC P CCG P CCU P CGA R CGC R CGG R CGU R CUA L CUC L CUG L CUU L GAA E GAC D GAG E GAU D GCA A GCC A GCG A GCU A GGA G GGC G GGG G GGU G GUA V GUC V GUG V GUU V UAA Z UAC Y UAG Z UAU Y UCA S UCC S UCG S UCU S UGA Z UGC C UGG W UGU C UUA L UUC F UUG L UUU F"
dict_codons_to_aminos = {}

def codons_to_amino_acids(string_Codons_aminos, dict_codons_to_aminos):	
	for i in range(len(string_Codons_aminos)-5):
		if i%6 == 0:
			codon = string_Codons_aminos[i:i+3] #  ; take three elements, every seven elements. 
			amino = string_Codons_aminos[i+4]
			dict_codons_to_aminos[codon] = amino #set the codon as key and amino acid as value
	return dict_codons_to_aminos

print codons_to_amino_acids(string_Codons_aminos, dict_codons_to_aminos)
print dict_codons_to_aminos["AGG"]


