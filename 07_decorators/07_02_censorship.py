# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(func):
    def remove_shoot(text):
        output = text.replace('Shoot', 'Sxxxx')
        return output
    return remove_shoot

@censor
def shooter(text):
    return text

print(shooter("I like to Shoot!"))