from flask import Flask, request
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.route('/')
def index():
    return "Welcome to the Flask Job Queue App! Use /enqueue?task=xyz"

@app.route('/enqueue')
def enqueue():
    task = request.args.get('task', 'default_task')
    r.rpush("jobs", task)
    return f"✅ Enqueued task: {task}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
