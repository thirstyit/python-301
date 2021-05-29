# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    def my_decorator2(func):
        def wrapper(*args):
            return f'{"".center(80, symbol)}\n{func(*args)}\n{"".center(80, symbol)}'
        return wrapper
    return my_decorator2


@decorate('*')
def asterix(sentence):
    return sentence


@decorate('%')
def percent(a):
    return a

print(asterix(input('Type in a sentence: ')))
print(percent(input('Type in another sentence: ')))