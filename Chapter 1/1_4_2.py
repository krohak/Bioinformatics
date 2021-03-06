# Copy your PatternMatching function below this line.

# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
def PatternMatching(Pattern, Genome):
    positions = []
    patternLen = len(Pattern)
    genomeLen = len(Genome)
    for i in range(genomeLen-patternLen+1):
        window = Genome[i:i+patternLen]
        positions.append(i) if window==Pattern else None    
    return positions

print(PatternMatching('CTTGATCAT', v_cholerae))

# print the positions variable