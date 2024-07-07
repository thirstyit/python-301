# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

f_handle = open(file_name, 'r')

total = 0

for line in f_handle.readlines():
    try:
        
        #line = line.strip()
        x = int(line)
        

    except IOError:
        print("Error on entry")
    except ValueError:
        print("Value Error")
    except:
        print("UnknowN Error")
        print(x)
    else:
        total += x
print(total)