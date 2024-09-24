import multiprocessing

def is_prime(n):
    """Returns True if n is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    """Checks if numbers in the given chunk are prime."""
    return [num for num in numbers if is_prime(num)]

def find_primes_in_range(numbers, chunk_size):
    """Finds prime numbers in the list using multiprocessing."""
    with multiprocessing.Pool() as pool:
        # Split the numbers into chunks and process them in parallel
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
        results = pool.map(check_prime_chunk, chunks)
    # Flatten the list of results
    return [prime for sublist in results for prime in sublist]