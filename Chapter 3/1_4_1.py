from operator import mul
from functools import reduce

def Pr(Text, Profile):
    return reduce(mul, [ Profile[t][i] for i, t in enumerate(Text) ])

def ProfileMostProbableKmer(text, k, profile):
    probs = [ Pr(text[window:window+k], profile) for window in range(len(text)-k+1) ]
    idx = [ i for i, x in enumerate(probs) if x==max(probs) ][0]
    return text[idx:idx+k]