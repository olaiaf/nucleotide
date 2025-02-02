import sys
from argparse import ArgumentParser

# Set up the argument parser
parser = ArgumentParser(description="Calculate the percentage of nucleotides in a DNA or RNA sequence.")
parser.add_argument("-s", "--seq", type=str, required=True, help="DNA or RNA sequence")
args = parser.parse_args()

# Convert the sequence to uppercase
seq = args.seq.upper()

# Verify that the sequence contains only valid characters
if any(base not in "ACGTU" for base in seq):
    print("Error: The sequence should only contain A, C, G, T (DNA) or U (RNA).")
    sys.exit(1)

# Calculate the percentage of each nucleotide
total = len(seq)
percentages = {base: seq.count(base) / total * 100 for base in "ACGTU"}

# If it's DNA, remove the percentage of U
if "U" not in seq:
    percentages.pop("U")

# If it's RNA, remove the percentage of T
if "T" not in seq:
    percentages.pop("T")

# Display the results
print("Nucleotide percentages:")
for base, percent in percentages.items():
    print(f"{base}: {percent:.2f}%")

