from flask import Flask, request
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.route('/')
def index():
    return "🔁 Flask App is Live! Use /enqueue?task=xyz"

@app.route('/enqueue')
def enqueue():
    task = request.args.get('task', 'default_task')
    r.rpush("jobs", task)
    return f"✅ Task '{task}' enqueued!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
