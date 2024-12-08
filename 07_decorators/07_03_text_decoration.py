# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************



def text_decorate(symbol):
    def dec_func(func):    
        def inner_text(text):
            output = func(text)
            output =  symbol*20 + "\n" + text + "\n" + symbol*20
            return output
        return inner_text
    return dec_func

    

@text_decorate("#")
def main_text(text):
    return text
    

print(main_text("Kodify"))

