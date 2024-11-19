"""Given a number N, can you fabricate the two numbers NE and NO such that NE is formed by even digits of N and NO is formed by odd digits of N? Examples:

input	NE	NO
126453	264	153
3012	2	31
4628	4628	0
0 is considered as an even number.

In C and JavaScript you should return an array of two elements such as the first is NE and the second is NO."""

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