from func_tools import *
import random

def main():
    test_sequence = ''.join([random.choice(nicleotides) for nuc in range(50 )])
    result = is_valid_nucleotide_sequence(test_sequence)
    if result:
        print(f"Valid sequence: {result}")
        counts = count_nucleotides(result)
        print("Nucleotide counts:", counts)
    else:
        print("Invalid nucleotide sequence.")


if __name__ == "__main__":
    main()