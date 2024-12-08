# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def quoter(func):
    def decorator_func(func):
        def inner_quoter(text):
            output = func(text)
            output = '"' + text + '"'
            return output
        return inner_quoter
    return decorator_func

@quoter
def hello(text):
    return text

print(hello("Hello World"))
