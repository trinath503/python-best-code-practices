class A:
    def __init__(self):
        self.price = 40
        
    def __add__(self, other):
        return self.price + other.price
class B:
    def __init__(self):
        self.price = 60

    

a = A()
b = B()
print(a + b)



class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return f"Vector({', '.join(str(c) for c in self.components)})"

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __setitem__(self, index, value):
        self.components[index] = value

    def __delitem__(self, index):
        del self.components[index]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length for addition.")
        result = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length for subtraction.")
        result = [x - y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def __eq__(self, other):
        return self.components == other.components

    def __lt__(self, other):
        return len(self.components) < len(other.components)


# Create two Vector instances
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Test various dunder methods
print(v1)  # Vector(1, 2, 3)
print(len(v1))  # 3
print(v1[0])  # 1
v1[1] = 10
print(v1 + v2)  # Vector(5, 15)
print(v1)  # Vector(1, 10, 3)
del v1[2]
print(v1)  # Vector(1, 10)

print(v2 - v1)  # Vector(3, 5)
print(v1 == v2)  # False
print(v1 < v2)  # True

#############################
# Different types of errors #
#############################

# TypeError: Raised when an operation or function is applied to an object of an inappropriate type.
# IndexError: Raised when a sequence subscript is out of range.
# KeyError: Raised when a dictionary key is not found.
# NameError: Raised when a local or global name is not found.
# FileNotFoundError: Raised when a file or directory is not found.
# ZeroDivisionError: Raised when division or modulo operation is performed with a divisor of zero.
# AttributeError: Raised when an attribute reference or assignment fails.
# OverflowError: Raised when the result of an arithmetic operation is too large to be expressed within the range of the integer type.
# AssertionError: Raised when an assert statement fails.
# StopIteration: Raised when the next() function is called on an iterator that has no further items.
# ValueError: Raised when a function receives an argument of the correct type but an invalid value.