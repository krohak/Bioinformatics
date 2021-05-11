from operator import mul
from functools import reduce

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    return [ ProfileMostProbableKmer(d, 4, Profile) for d in Dna ]

# Insert your ProfileMostProbablePattern(Text, k, Profile) and Pr(Pattern, Profile) functions here.
def Pr(Text, Profile):
    return reduce(mul, [ Profile[t][i] if t in Profile else 1 for i, t in enumerate(Text) ])

def ProfileMostProbableKmer(text, k, profile):
    probs = [ Pr(text[window:window+k], profile) for window in range(len(text)-k+1) ]
    idx = [ i for i, x in enumerate(probs) if x==max(probs) ][0]
    return text[idx:idx+k]