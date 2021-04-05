class MyError(Exception):
    pass


class AgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"You'll be born in {abs(self.age)} years."

age = int(input("Age: "))
try:
    if age < 0:
        raise AgeError(age)
except AgeError as ae:
    print(ae.age)
    print(ae.message)


# class AgeError(Exception):
#     def __init__(self, age):
#         self.age = age


# age = int(input("Age: "))

# try:
#     if age < 0:
#         raise AgeError(age)
# except AgeError as ae:
#     print(f"This might be a miracle. They say they're {ae.age} years old.")


# Traceback (most recent call last):
#   File "<input>", line 2, in <module>
#     raise AgeError(age)
# AgeError: -1


# import sys

# class SomeException(Exception):
#     pass

# class OtherException(Exception):
#     pass

# try:
#     raise SomeException
# except SomeException as s:
#     tb = sys.exc_info()[2]
#     breakpoint()
#     raise OtherException("whazzup").with_traceback(s)  #tb