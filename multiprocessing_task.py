import multiprocessing

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    """Check a chunk of numbers for primes."""
    return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
    """Find prime numbers in the provided range using multiprocessing."""
    with multiprocessing.Pool() as pool:
        # Split the numbers into chunks
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
        # Map the check_prime_chunk function to the chunks
        results = pool.map(check_prime_chunk, chunks)
        # Flatten the list of results
        primes = [prime for sublist in results for prime in sublist]
    return primes