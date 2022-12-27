s1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
s2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
transitions, transversion = 0, 0
cg = ['C','G']
at = ['A', 'T']

for x,y in zip(s1,s2):
    if x != y and x in cg and y in cg:
        transitions += 1
    elif x != y and x in at and y in at:
        transitions += 1
    elif x in at and y in cg:
        transversion += 1
    elif x in cg and y in at:
        transversion += 1
        
print(transitions / transversion)