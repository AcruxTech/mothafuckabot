def get_reversed_number(number: int) -> int:
    return int(str(number).rjust(2, '0')[::-1])