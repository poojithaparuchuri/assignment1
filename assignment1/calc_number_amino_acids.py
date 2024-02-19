"""
    Sree Poojitha Paruchuri
    File: calc_number_amino_acids.py
"""
import sys

# !/usr/bin/python

def calculate_dna_sequence(sequence_len):
    """
         calculating amino acids
        function - analysing DNA sequences
    """
    # Check if the sequence length is divisible by 3
    if sequence_len % 3 != 0:
        print("\nError: the DNA sequence is not a multiple of 3", file=sys.stderr)
        sys.exit(1)

    # To calculate the number of amino acids
    amino_acids = sequence_len // 3

    # To estimate the molecular weight in Kilo Da
    # 110 Daltons per amino acid, converted to Kilo Da
    mol_weight = amino_acids * 110 / 1000
    return amino_acids, mol_weight


def main():
    """Ask the user for the name of the DNA sequence and then display results"""
    sequence_name = input("Please provide a name for the DNA sequence: ")
    print("Your sequence name is:", sequence_name)

    # Ask the user for the length of the DNA sequence
    sequence_len = int(input("Please enter the sequence length: "))

    if calculate_dna_sequence(sequence_len) is not None:

        # Calculate protein-related information
        amino_acids, mol_weight = calculate_dna_sequence(sequence_len)

        print("The length of the DNA sequence is:", sequence_len)
        print("The number of decoded amino acids is:", amino_acids)
        print("The average weight of the protein sequence is: {:.2f}".format(mol_weight))

    # if amino_acids is not None and mol_weight is not None:
    # Display the results


if __name__ == "__main__":
    main()
