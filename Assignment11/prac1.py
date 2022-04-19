'''
You are given a string. Your task is to count the frequency of letters of 
the string and print the letters in descending order of frequency.
If the following string is given as input to the program:

Input:
aabbbccde

Output:
b 3 a 2 c 2 d 1 e 1
'''
def frequency(str):
    dict={}
    for n in str:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict

s=input('Enter a string : ')
print()
print(frequency(s))