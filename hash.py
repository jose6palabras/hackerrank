def sieve(limit):
    if limit < 2:
        return []

    if limit == 2:
        return [False, True]

    if limit == 3:
        return [False, True, True]
    
    res = [False]*limit

    i = 1
    while i <= limit:
        j = 1
        while j <= limit:
            n = (4 * i * i) + (j * j)
            if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                res[n] = True
            n = (3 * i * i) + (j * j)
            if n <= limit and n % 12 == 7:
                res[n] = True
            n = (3 * i * i) - (j * j)
            if (i > j and n <= limit and n % 12 == 11):
                res[n] = True
            j += 1
        i += 1
    r = 5
    while r*r < limit:
        if res[r]:
            for i in range(r*r, limit, r*r):
                res[i]= False
        r += 1
    return res

def pick_prime(primes, min_size=1000):
    """returns a suitable prime to use as modulus"""
    for prime in primes:
        if prime >= min_size:
            return prime
    # if no prime large enough exists, use last one on list
    return primes[-1]

def hash(string, modulus):
    """implements polynomial rolling of string keys"""
    p_value = 29791
    l_s = len(string)
    hash_v_o = 0
    for i in range(0, l_s):
        hash_v_o = hash_v_o + ord(string[i])*p_value**i
    return hash_v_o % modulus

if __name__ == '__main__':
    # generate primes list to use as modulus
    primes = sieve(10000) # modify limit based on your needs
    modulus = pick_prime(primes, 1000)
    test_array = ["alpha","beta","gamma","delta","epsilon"]

    for string in test_array:
        hash_value = hash(string, modulus)
        print(f"Hash of {string} is {hash_value}")

