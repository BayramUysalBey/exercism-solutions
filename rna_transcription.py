"""Your task is to determine the RNA complement of a given DNA sequence.

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G), and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G), and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G -> C
C -> G
T -> A
A -> U"""

# My solution
def to_rna(dna_strand):
    package = {
        "A": "U",
        "C": "G",
        "G": "C",
		"T": "A"
	}
    return ''.join(package[nucleotide] for nucleotide in dna_strand if nucleotide in package)