from ctypes import *

path = './functions.dll'
functions = cdll.LoadLibrary(path)

print(vars(functions))

print(functions.add(1, 3))

print(functions.mult(2, 5))