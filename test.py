# Rosalind / SSEQ (Fra)

from Bio import SeqIO

with open('/Users/Shared/Rosalind/rosalind_sseq.txt', 'r') as my_file:
    l = [x.seq for x in SeqIO.parse(my_file, 'fasta')]  
    s1, s2, subs, start  = str(l[0]), str(l[1]), [], 0
    star_len = len(s1)
    for i in range(len(s2)):
        start = s1.index(s2[i])
        subs.append(start - len(s1) + star_len + 1)
        s1 = s1[start+1:]
    print(*subs)