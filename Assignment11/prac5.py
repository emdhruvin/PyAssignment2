'''
explain about the different type of exceptions in python with
suitable example
'''
# arithmatic exeption
import imp
import math

from numpy import arange


try:
    a=5/0
    print(a)
except ArithmeticError:
    print('Arithmatic Exception')
else :
    print('success')

#index out of bond
try:
    a=[1,2,3,4]
    print(a[43])
except LookupError:
    print('Array Index out of bound')

#Attribute Error
class Attributes(object):
    pass
object=Attributes()
print(object.attribute)

#floating pointer error
import math
print(math.exp(1000))

#index error
array=[0,1,2]
print(array[3])