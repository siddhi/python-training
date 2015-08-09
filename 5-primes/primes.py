def is_3xplus1(num):
    return (num - 1) % 3 == 0


def get_primes():
    num = 2
    prime_list = []

    def is_prime(num):
        for factor in prime_list:
            if num % factor == 0:
                return False
        return True

    while True:
        if is_prime(num):
            prime_list.append(num)
            yield num
        num = num + 1

other_primes = (prime for prime in get_primes() if is_3xplus1(prime))
for prime, other_prime in zip(get_primes(), other_primes):
    print(prime, other_prime)
