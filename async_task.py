import asyncio

async def async_io_task(filename):
    print(f"Starting Async I/O task for {filename}")
    await asyncio.sleep(1)  
    print(f"Completed Async I/O task for {filename}")

async def run_async_tasks():
    tasks = [
        async_io_task('file1.txt'),
        async_io_task('file2.txt'),
        async_io_task('file3.txt')
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run_async_tasks())