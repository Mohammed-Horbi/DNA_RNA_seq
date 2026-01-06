import collections
nicleotides = ['A', 'T', 'C', 'G', 'U']

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
