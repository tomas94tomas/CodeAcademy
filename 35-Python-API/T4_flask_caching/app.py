from flask import Flask, render_template
from flask_caching import Cache
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['CACHE_TYPE'] = 'SimpleCache'  # In-memory cache (for demo)
app.config['CACHE_DEFAULT_TIMEOUT'] = 30  # seconds

cache = Cache(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/slow')
def slow():
    start = time.time()
    time.sleep(3)  # Simulate slow work
    elapsed = time.time() - start
    return f"Slow route! Took {elapsed:.2f} seconds (no cache)"

@app.route('/cached')
@cache.cached()
def cached():
    start = time.time()
    time.sleep(3)  # Simulate slow work
    elapsed = time.time() - start
    return f"Cached route! Took {elapsed:.2f} seconds (with cache)"

if __name__ == '__main__':
    app.run(debug=True)
