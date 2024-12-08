# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".


def censor(*args):
    def censor_args(func):
        def remove_shoot(text):
            output = func(text)
            output = text.replace(args[0], 'Sxxxx')
            output = output.replace(args[1], 'cxxx')
            return output
        return remove_shoot
    return censor_args

@censor("Shoot", "crab")
def shooter(text):
    return text

print(shooter("I like to Shoot and eat crabs!"))