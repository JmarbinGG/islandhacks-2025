from math import gcd

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE = len(ALPHABET)
LENGTH = 6
MOD = BASE ** LENGTH          

a = 35450549
b = 2750043
assert gcd(a, MOD) == 1

def base62_encode(n: int) -> str:
    s = []
    for _ in range(LENGTH):
        n, r = divmod(n, BASE)
        s.append(ALPHABET[r])
    return "".join(reversed(s))

def base62_decode(s: str) -> int:
    n = 0
    for ch in s:
        n = n * BASE + ALPHABET.index(ch)
    return n

def int_to_code(x: int) -> str:
    y = (a * x + b) % MOD
    return base62_encode(y)

def code_to_int(code: str) -> int:
    y = base62_decode(code)
    a_inv = pow(a, -1, MOD)
    return (a_inv * (y - b)) % MOD

