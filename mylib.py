import math
import random

global chrshift
chrshift = 1300


def mod_pow(a, b, n):
    bin_b = list(bin(b)[3:])

    a0 = a

    for i in bin_b:
        if i == '1':
            a = a * a * a0 % n
        else:
            a = a**2 % n

    return a


def mod_pow1(a, b, n):
    bin_b = list(bin(b)[3:])

    a0 = a

    for i in bin_b:
        if i == '1':
            a = a * a * a0 % n
        else:
            a = a * a % n

    return a


def jacobi(a, b):
    if math.gcd(a, b) != 1:
        return 0

    r = 1

    if a < 0:
        a = -a
        if b % 4 == 3:
            r = -r

    while a != 0:
        t = 0
        while a % 2 == 0:
            t += 1
            a /= 2

        if t % 2 != 0:
            if b % 8 == 3 or b % 8 == 5:
                r = -r

        if a % 4 == 3 and b % 4 == 3:
            r = -r

        c = a
        a = b % c
        b = c
    return r


def prime_test(n, k):
    for i in range(1, k):
        a = random.randrange(n - 1) + 1

        if math.gcd(a, n) > 1 or mod_pow(a, round((n - 1) // 2), n) != (jacobi(a, n)) % n:
            # print("составное")
            return False

    # print("простое, вероятность ошибки : ", 2 ** (-k))
    return True


def rand_prime(size):
    # p = random.randint(2 ** (size - 1), 2 ** size)
    # while not prime_test(p, 20):
    #    p = random.randint(2 ** (size - 1), 2 ** size)
    # return p
    p = random.randint(1, 2 ** size) + 2 ** size
    while not prime_test(p, 5):
        p = random.randint(1, 2 ** size) + 2 ** size
    return p


def rand_prime_range(a, b):
    # p = random.randint(2 ** (size - 1), 2 ** size)
    # while not prime_test(p, 20):
    #    p = random.randint(2 ** (size - 1), 2 ** size)
    # return p
    p = random.randint(a, b)
    while not prime_test(p, 5):
        p = random.randint(a, b)
    return p


def ordify(text):
    string = ""
    for t in text:
        o = ord(t) + 1300

        string += str(o)
    return int(string)


def str_parts(text, l):
    i = 0
    out = []
    while i < len(text):
        if i + l < len(text):
            t = text[i:i + l]
            out.append(ordify(t))
        else:
            out.append(ordify(text[i:len(text)]))
        i += l
    return out


def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return x, y


def gcd_ext(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q
    return a


def open_exp(fi):
    e = random.randint(1, fi)
    while gcd_ext(e, fi) != 1:
        e = random.randint(1, fi)
    return e


def chrify(c):
    return chr(c - 1300)


def strify(lst):
    out = ""
    l = 4
    for i in range(len(lst)):
        lst[i] = str(lst[i])

    for i in lst:
        j = 0
        while j < len(i):
            out += (chr(int(i[j:j + l]) - chrshift))
            j += l
    return out
