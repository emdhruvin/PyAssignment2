'''
Given a list of integers, write a program to print the count of all possible unique 
combinations of numbers whose sum is equal to K. Input The first line of input 
will contain space-separated integers. The second line of input will contain an integer, 
denoting K. Output The output should be containing the count of all unique combinations
 of numbers whose sum is equal to K.

Sample Input 1 2 4 6 1 3 6 
Sample Output 1 3

'''
from itertools import combinations
numbers=[int(n) for n in input('Enter an array : ').split()]
k=int (input('Enter the sumation you want to check combination about : '))
count =0
for i in range (1,len(numbers)+1):
    for c in combinations(numbers,i):
        if sum(c)==k:
            count+=1

print(count)