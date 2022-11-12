def to_binary(n):
    d = ''
    while n > 0:
        d += str(n % 2)
        n //= 2
    return int(d[::-1])
