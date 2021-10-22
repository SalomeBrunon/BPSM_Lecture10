#!/usr/local/bin/python3

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
count_A = dna_seq.count("A")
count_T = dna_seq.count("T")
length = len(dna_seq)
A_T_content = (count_A + count_T) / length
print("The A and T content of the DNA sequence is " + str(A_T_content))

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement_seq = ""
for i in my_dna:
	if i == "A":
		complement_seq += "T"
	elif i == "T":
                complement_seq += "A"
	elif i == "C":
		complement_seq += "G"
	elif i == "G":
		complement_seq += "C"

print(complement_seq)

print("The complement sequence is", my_dna.replace('A', 't').replace('T','a').replace('G','c').replace('C','g').upper())

my_dna2 = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print("The position of the cut is", my_dna2.find("GAATTC"))
first_frag = my_dna[:22] 
second_frag = my_dna[22:]
print("first frag", len(first_frag), "second frag", len(second_frag))

genomic_DNA = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon_1 = genomic_DNA[:63]
intro = genomic_DNA[63:90]
exon_2 = genomic_DNA[90:]
coding_sequence = exon_1+exon_2
length_genomic = len(genomic_DNA)
percentage_coding = len(coding_sequence)/length_genomic*100
print("The percentage of the DNA sequence that is coding is", percentage_coding)
print("Seq " + exon_1 + intro.lower()+ exon_2)
