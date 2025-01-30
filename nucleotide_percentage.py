import sys
from argparse import ArgumentParser

# Create the argument parser
parser = ArgumentParser(description="Compute the percentage of each nucleotide in a DNA or RNA sequence.")
parser.add_argument("-s", "--seq", type=str, required=True, help="Input DNA or RNA sequence")
args = parser.parse_args()

# Convert to uppercase and validate that the sequence is valid
seq = args.seq.upper()

if not all(base in 'ACGTU' for base in seq):
    print("Error: The sequence should only contain the letters A, C, G, T (DNA) or U (RNA).")
    sys.exit(1)

# Function to calculate the nucleotide percentages
def calculate_percentages(sequence):
    total = len(sequence)
    percentages = {
        'A': sequence.count('A') / total * 100,
        'C': sequence.count('C') / total * 100,
        'G': sequence.count('G') / total * 100,
        'T': sequence.count('T') / total * 100,
        'U': sequence.count('U') / total * 100,
    }
    
    # If the sequence is DNA, remove 'U' from the calculation
    if 'U' not in sequence:
        del percentages['U']
    
    return percentages

# Calculate and display the results
percentages = calculate_percentages(seq)
print(f"Nucleotide percentages in the sequence:")
for nucleotide, percentage in percentages.items():
    print(f"{nucleotide}: {percentage:.2f}%")
