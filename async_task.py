import asyncio

async def async_write_to_file(filename, data):
    """Asynchronously writes data to a file."""
    await asyncio.sleep(0)  # Simulate non-blocking I/O
    with open(filename, "a") as f:
        for item in data:
            f.write(f"{item}\n")

async def run_async_tasks(primes):
    """Run asynchronous file writing tasks."""
    await async_write_to_file("primes_number.txt", primes)