from func_tools import *
import random

def main():
    test_sequence = ''.join([random.choice(nicleotides) for nuc in range(50 )])
    result = is_valid_nucleotide_sequence(test_sequence)
    if result:
        print(f"Valid sequence: {result}")
        print(f"Sequence length: {len(result)}")
        counts = count_nucleotides(result)
        print("Nucleotide counts:", counts)
        print(f"Original sequence and Reverse complement:\n5 {colored_seq(result)} 3")
        print(f"  {''.join('|' for _ in result)}")
        dna_reverse_complement = reverse_complement(result)
        print(f"3 {colored_seq(dna_reverse_complement)} 5")
        rna_sequence = transcribe_dna_to_rna(result)
        print("Transcribed RNA sequence:", colored_seq(rna_sequence))
    else:
        print("Invalid nucleotide sequence.")


if __name__ == "__main__":
    main()