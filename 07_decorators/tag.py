def tagify(tag):
    def decorator_tagify(func):
        def wrapping(*args):
            return f'<{tag}>{func(*args)}</{tag}>'
        return wrapping
    return decorator_tagify


# text = input("What do you want to wrap? ")
# tag = input("What tag do you want to use? ")


@tagify('p')
def say(msg):
    # do anything
    return msg

@tagify('strong')
def scream(word):
    return word.upper()


@tagify('dic')
def combine(word1, word2):
    return word1 + word2

print(say("hello"))
print(scream("hello"))
print(combine("hello", "there"))