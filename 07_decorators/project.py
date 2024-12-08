def tagify(*args):
    def wrapper(func):
        def inner(text):
            output = func(text)
            output = "<" + args[0] + ">" + text + "</" + args[0] + ">"
            return output
        return inner
    return wrapper

@tagify("div")
def greet(name):
    return f"Hello, {name}"





print(greet("Bessy"))