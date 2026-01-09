import collections
nicleotides = ['A', 'T', 'C', 'G']

def is_valid_nucleotide_sequence(sequence):
    """Check if the given sequence contains only valid nucleotides."""
    sequence = sequence.upper()
    for char in sequence:
        if char not in nicleotides:
            return False
    return sequence

def count_nucleotides(sequence):
    """Count the occurrences of each nucleotide in the sequence."""
    sequence = sequence.upper()
    # we can use this approach instead of collections.Counter
    # counts = {nuc: 0 for nuc in nicleotides}
    # for char in sequence:
    #     if char in counts:
    #         counts[char] += 1
    # return counts
    # or we can use collections.Counter directly
    return dict(collections.Counter(sequence))

def transcribe_dna_to_rna(sequence):
    sequence = sequence.upper()
    return sequence.replace('T', 'U')

def reverse_complement(sequence):
    """Get the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    sequence = sequence.upper()
    rev_comp = ''.join(complement[base] for base in reversed(sequence))
    return rev_comp

def colored_seq(sequence):
    sequence = sequence.upper()
    # ANSI colors (works in many terminals)
    m = {
        "A": "\033[31mA\033[0m",  # red
        "C": "\033[34mC\033[0m",  # blue
        "G": "\033[32mG\033[0m",  # green
        "T": "\033[33mT\033[0m",  # yellow
        "U": "\033[33mU\033[0m",  # yellow
        # "N": "\033[90mN\033[0m",  # gray
    }
    return "".join(m.get(ch.upper(), ch) for ch in sequence)

def gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100 if len(sequence) > 0 else 0

def gc_content_subsequence(sequence, window_size):
    """window_size indicates the size or length of each subsequence."""
    """Calculate GC content in sliding windows or subsequences across the sequence."""
    sequence = sequence.upper()
    gc_contents = []
    for i in range(0, len(sequence) - window_size + 1, window_size):
        sub_seq = sequence[i:i + window_size]
        gc_contents.append(gc_content(sub_seq))
    return gc_contents