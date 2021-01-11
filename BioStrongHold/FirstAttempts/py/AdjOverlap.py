# This program with compute the adjacency matrix corresponding to an 
# overlap graph for strings of length k. 

from Bio import SeqIO

def main(fasta_file,k):
    dna_ids = []
    dna_strings = []
    adjList = dict()
    # Read fasta file and get both the ids and the strings themselves
    with open(fasta_file) as f:
        for fasta in SeqIO.parse(f,'fasta'):
            dna_ids.append(str(fasta.id))
            dna_strings.append(str(fasta.seq))
    # Iterate over the dna strings and check suffix against all others
    dna_idx = 0
    for dna in dna_strings:
        check_dna_idx = 0
        adjMatches = []
        for check_dna in dna_strings:
            if check_dna[:k] == dna[-k:] and check_dna != dna:
                adjMatches.append(dna_ids[check_dna_idx])
            check_dna_idx+=1
        adjList[dna_ids[dna_idx]] = adjMatches
        dna_idx+=1

    for k,v in adjList.items():
        for i in v: print(k,i)

if __name__ == '__main__':
    a = input("What length of overlap should we look for?: ")
    k = int(a)
    main(r'rosalind_grph.txt',k)
