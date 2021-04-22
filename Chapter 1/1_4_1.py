# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    return Reverse(Complement(Pattern))

def Reverse(Pattern):
    return ''.join(list(reversed(Pattern)))

def Complement(Pattern):
    complementMap = {'A':'T','T':'A','G':'C','C':'G'}
    return ''.join([complementMap[c] for c in Pattern])