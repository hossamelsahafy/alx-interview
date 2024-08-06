#!/usr/bin/python3
"""
    Prime Game
"""


def isWinner(x, nums):
    """Is Winner Method"""
    if x <= 0 or not nums:
        return None

    def sieve(n):
        """Sieve Method"""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] == True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0], is_prime[1] = False, False
        return [p for p in range(n + 1) if is_prime[p]]

    max_num = max(nums)
    primes = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        if not primes_in_game:
            ben_wins += 1
            continue

        turn = 0
        while primes_in_game:
            prime = primes_in_game.pop(0)
            primes_in_game = [p for p in primes_in_game if p % prime != 0]
            turn += 1

        if turn % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
