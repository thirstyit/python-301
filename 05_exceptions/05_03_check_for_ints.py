# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

v = True


while(v) :
    try:
        x = int(input("Enter a number: ")) 
    except ValueError:
        print("Integers only bro.")
    else:
        v = False
        
        