import redis
import time
import os

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

print("🔧 Worker is running and waiting for jobs...")

while True:
    job = r.lpop("jobs")
    if job:
        print(f"🛠️ Processing job: {job}")
    time.sleep(1)
