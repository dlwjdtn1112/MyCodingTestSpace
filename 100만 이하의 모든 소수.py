def sieve_of_eratosthenes(limit):

    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False




    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False  # num의 배수는 소수가 아님




    return [num for num, is_prime in enumerate(sieve) if is_prime]


limit = 1000000
primes = sieve_of_eratosthenes(limit)
for lst in primes:
    print(lst,end = " ")
