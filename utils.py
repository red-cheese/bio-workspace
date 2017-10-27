

ADENINE = A = 'A'
CYTOSINE = C = 'C'
GUANINE = G = 'G'
THYMINE = T = 'T'

URACIL = U = 'U'

PURINES = [A, G]
PYRIMIDINES = [C, T, U]

DNA_COMPLEMENTS = {A: T, T: A, C: G, G: C}
RNA_COMPLEMENTS = {A: U, U: A, C: G, G: C}


PROT_START_CODON = 'AUG'

PROT_CODON_TABLE = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': -1,       'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': -1,       'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': -1,       'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G',
}

PROT_MASS_TABLE = {
    'A':   71.03711,
    'C':   103.00919,
    'D':   115.02694,
    'E':   129.04259,
    'F':   147.06841,
    'G':   57.02146,
    'H':   137.05891,
    'I':   113.08406,
    'K':   128.09496,
    'L':   113.08406,
    'M':   131.04049,
    'N':   114.04293,
    'P':   97.05276,
    'Q':   128.05858,
    'R':   156.10111,
    'S':   87.03203,
    'T':   101.04768,
    'V':   99.06841,
    'W':   186.07931,
    'Y':   163.06333,
}


def first_line(f):
    return next(f).strip()


def read_fasta(f, dna_only=False):
    dnas = []

    id_, dna = None, ''

    for line in f:
        line = line.strip()

        if line.startswith('>'):
            # Flush the old ID and DNA.
            if id_ is not None:
                dnas.append((id_, dna))
                dna = ''

            id_ = line[1:]  # Strip the '<' symbol.
        else:
            dna += line

    # Flush the last one.
    if id_ is not None:
        dnas.append((id_, dna))

    return dnas if not dna_only else [dna for _, dna in dnas]
