def announce(msg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Before: {msg}")
            result = func(*args, **kwargs)
            print(f"After: {msg}")
            return result
        return wrapper
    return decorator

@announce("Special operation")
def do_something():
    print("Doing something important.")

if __name__ == "__main__":
    do_something()
