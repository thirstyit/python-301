# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".


import os



path_name = 'books/'
for file in os.listdir(path_name):

    try:
        f_handle = open(path_name + file, 'r')
        chars = f_handle.read(100)
        if 'Prince' in chars:
            print(file)
            raise PrinceException
        
        

    except Exception as PrinceException:
        print('Prince of Persia')