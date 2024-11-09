def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify(frac):
    common_divisor = gcd(frac[0], frac[1])
    return [frac[0] // common_divisor, frac[1] // common_divisor]

def add_frac(frac1, frac2):
    result = [frac1[0]*frac2[1] + frac2[0]*frac1[1], frac1[1]*frac2[1]]
    return simplify(result)

def sub_frac(frac1, frac2):
    result = [frac1[0]*frac2[1] - frac2[0]*frac1[1], frac1[1]*frac2[1]]
    return simplify(result)

def mul_frac(frac1, frac2):
    result = [frac1[0]*frac2[0], frac1[1]*frac2[1]]
    return simplify(result)

def div_frac(frac1, frac2):
    result = [frac1[0]*frac2[1], frac1[1]*frac2[0]]
    return simplify(result)

def is_positive(frac):
    return frac[0] * frac[1] > 0

def is_zero(frac):
    return frac[0] == 0

def cmp_frac(frac1, frac2):
    return frac1[0]*frac2[1] - frac2[0]*frac1[1]

def frac2float(frac):
    return frac[0] / frac[1]