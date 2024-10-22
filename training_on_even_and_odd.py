def even_and_odd(n):
    NE = ''
    NO = ''
    for digit in str(n):
        if int(digit) % 2 == 0:
            NE += digit
        else:
            NO += digit
    NE = int(NE) if NE else 0
    NO = int(NO) if NO else 0
    return NE, NO