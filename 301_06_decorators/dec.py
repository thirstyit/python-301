def decorator_func(initial_func):
    def wrapper_func(*args):
        print("wrapper function picked some...")
        return initial_func(*args)
    return wrapper_func

@decorator_func
def prettify(msg):
    print(msg)

@decorator_func
def feed(carbs, protein):
    print(f"{carbs} and {protein}")

prettify("flowers for you")
feed("bread", "lentils")