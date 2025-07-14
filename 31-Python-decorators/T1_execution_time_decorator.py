import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@execution_time
def sample_function():
    time.sleep(1)
    print("Function executed.")

if __name__ == "__main__":
    sample_function()
