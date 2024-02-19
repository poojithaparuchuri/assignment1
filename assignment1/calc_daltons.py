"""
    Sree Poojitha Paruchuri
    File: calc_daltons.py
"""
def calculate_molecular_weight(protein_sequence, average_molecular_weight_per_aminoacid):
    """Calculate the molecular weight of a protein sequence"""

    # Calculate the length of the protein sequence
    protein_seq_len = len(protein_sequence)

    # Calculate the total molecular weight in kilodaltons
    total_molecular_weight = (protein_seq_len * average_molecular_weight_per_aminoacid) / 1000

    return protein_seq_len, total_molecular_weight


def main():
    """Main function to calculate the molecular weight of a protein sequence"""

    # Hard coded protein sequence
    protein_sequence = """MADPAAGPPPSEGEESTVRFARKGALRQKNVHEVKNHKF\
TARFFKQPTFCSHCTDFIWGFGKQGFQCQVCCFVVHKRCHEFVTFSCPGADKGPA\
SDDPRSKHKFKIHTYSSPTFCDHCGSLLYGLIHQGMKCDTCMMNVHKRCVMNVPS\
LCGTDHTERRGRIYIQAHIDREVLIVVVRDAKNLVPMDPNGLSDPYVKLKLIPDP\
KSESKQKTKTIKCSLNPEWNETFRFQLKESDKDRRLSVEIWDWDLTSRNDFMGSL\
SFGISELQKAGVDGWFKLLSQEEGEYFNVPVPPEGSEGNEELRQKFERAKIGQGT\
KAPEEKTANTISKFDNNGNRDRMKLTDFNFLMVLGKGSFGKVMLSERKGTDELYA\
VKILKKDVVIQDDDVECTMVEKRVLALPGKPPFLTQLHSCFQTMDRLYFVMEYVN\
GGDLMYHIQQVGRFKEPHAVFYAAEIAIGLFFLQSKGIIYRDLKLDNVMLDSEGH\
IKIADFGMCKENIWDGVTTKTFCGTPDYIAPEIIAYQPYGKSVDWWAFGVLLYEM\
LAGQAPFEGEDEDELFQSIMEHNVAYPKSMSKEAVAICKGLMTKHPGKRLGCGPE\
GERDIKEHAFFRYIDWEKLERKEIQPPYKPKARDKRDTSNFDKEFTRQPVELTPT\
DKLFIMNLDQNEFAGFSYTNPEFVINV"""

    # Input average molecular weight per amino acid (in daltons)
    average_molecular_weight_per_aminoacid = 110

    # Calculate the molecular weight
    protein_seq_len, total_molecular_weight = (calculate_molecular_weight
                                               (protein_sequence,
                                                average_molecular_weight_per_aminoacid))

    # Printing out the length and average weight of the protein
    print(f"The length of the protein sequence is: {protein_seq_len}")
    print(f"The average weight of this protein sequence in kilodaltons : {total_molecular_weight}")


if __name__ == "__main__":
    main()
