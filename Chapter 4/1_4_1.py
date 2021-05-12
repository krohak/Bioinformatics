def Normalize(Probabilities):
    return { k: p/sum(Probabilities.values()) for k, p in Probabilities.items() }

import random
from bisect import bisect_left

def WeightedDie(Probabilities):
    keys = list(Probabilities.keys())
    vals = list(Probabilities.values())
    cumm = [vals[0]]
    for i in range(1, len(vals)):
        cumm.append(vals[i]+cumm[-1])    
    idx = bisect_left(cumm, random.uniform(0,1))
    return keys[idx]