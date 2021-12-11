import random
import math
import mylib


def primitive_root(p):
    fact = []
    phi = p - 1
    n = phi
    i = 2
    while i * i <= n:
        if n % i == 0:
            fact.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        fact.append(n)

    res = 2
    while res <= p:
        ok = True
        i = 0
        while i < len(fact) and ok:
            ok = ok and mylib.mod_pow(res, phi // fact[i], p) != 1
            i += 1
        if ok: return res
        res += 1

    return -1


text = input()

p = mylib.rand_prime(55)
g = primitive_root(p)
x = random.randint(1, p - 1)
y = mylib.mod_pow(g, x, p)

print('открытый ключ:', 'y:', y, 'g:', g, 'p:', p)
print('закрытый ключ:', 'x', x)

lst = mylib.str_parts(text, 3)
for i in range(len(lst)):
    lst[i] = int(lst[i])

k = random.randint(1, p - 1)
while mylib.gcd_ext(k, p - 1) != 1:
    k = random.randint(1, p - 1)

c = [[0] * 2 for i in range(len(lst))]
i = 0
for M in lst:
    c[i][0] = mylib.mod_pow(g, k, p)
    c[i][1] = (mylib.mod_pow(y, k, p) * M % p) % p
    i += 1
M1 = []
for i in range(len(c)):
    M1.append(
        (mylib.mod_pow(c[i][1], 1, p) * mylib.mod_pow(c[i][0], (p - 1 - x), p)) % p
    )

print('текст:', lst)

print()
print('шифротекст:', c)
print()

print('расшифрованный текст:')
print(M1)
print(mylib.strify(M1))
