def get_reversed_number(number: int) -> int:
    return int(str(number).rjust(2, '0')[::-1])


def to_fence_font(seq: str) -> str:
    seq = list(seq.lower())
    for i, symbol in enumerate(seq):
        if not symbol.isalpha():
            continue
        if sum(map(str.isalpha, seq[:i])) % 2 == 0:
            seq[i] = symbol.upper()
        
    return ''.join(seq)