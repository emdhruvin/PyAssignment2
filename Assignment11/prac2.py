'''
Write a procedure to find min, max, mean, standard deviation, variance of number list.

Example
Input: 10 25 3 25 24 6
output: 4 80 37.13 27.25 848.70
'''
from re import A
import statistics
import pandas as pd

ser=pd.Series([10,25,3,25,24,6])
mean=ser.mean()
median=ser.median()
mode=ser.mode()
ran=ser.max()-ser.min()
deviation=ser.std(axis=0,skipna=True)

print('mean : ',mean,'\n')
print('median : ',median,'\n')
print('mode : ',mode,'\n')
print('range : ',ran,'\n')
print('standard deviation : ',deviation,'\n')
print('variance of sample set is % s'%(statistics.variance(ser))) 