'''Swap two numbers without using a temporary variable
 Input:integer a = "10", b = "50".'''
a = 10
b = 50

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)

