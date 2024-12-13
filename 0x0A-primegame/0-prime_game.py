#!/usr/bin/python3


""" prime game implementation """


def isWinner(x, nums):
    """
    Determines the winner of the prime number game.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben"),
             or None if there is a tie.
    """
    def sieve(n):
        """Generates a list of primes up to n using
        the Sieve of Eratosthenes."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    if not nums or x < 1:
        return None

    # Precompute the primes for the maximum value of n in nums
    max_n = max(nums)
    is_prime = sieve(max_n)
    prime_counts = [0] * (max_n + 1)

    # Count cumulative primes up to each number
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    # Simulate the game
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
