import asyncio
import random
import time

async def health_check(shard_id):
    await asyncio.sleep(random.uniform(0.2, 1.5))
    return True

async def main():
    start = time.perf_counter()
    tasks = [asyncio.create_task(health_check(i)) for i in range(10)]
    results = await asyncio.gather(*tasks)
    healthy = sum(results)
    elapsed = time.perf_counter() - start

    print(f"Total healthy shards: {healthy}/{len(results)}")
    print(f"Elapsed time: {elapsed:.2f}s")

asyncio.run(main())