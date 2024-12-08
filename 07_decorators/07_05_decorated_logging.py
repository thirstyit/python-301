# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

from datetime import datetime

def log_it(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} was called at {datetime.now()}\n")
        return result
    return wrapper




@log_it
def shooter(text):
    return text

print(shooter("I like to Shoot and eat crabs!"))