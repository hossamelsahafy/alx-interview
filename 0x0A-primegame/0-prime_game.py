#!/usr/bin/python3
"""
    Prime Game
"""
def isWinner(x, nums):
    """Is Winner"""
    def generate_primes(max_n):
        """Generate  Primes"""
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if (is_prime[p] == True):
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, max_n + 1) if is_prime[p]]

    def simulate_game(n):
        """Simulate Game"""
        primes = generate_primes(n)
        is_in_game = [True] * (n + 1)
        moves = 0
        
        for prime in primes:
            if prime > n:
                break
            if is_in_game[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    is_in_game[multiple] = False
        
        return 'Maria' if moves % 2 == 1 else 'Ben'

    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = simulate_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
