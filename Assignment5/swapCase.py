'''
AIM:
You are given a string and your taks is to swap case, in other word, convert all
lower case letters to upper and vice versa 

Sample input:
HackerRank.com present "Pythonist2".

Sample output:
hACKERrANK.COM PRESENT "pYTHONIST2".
'''
#solution
string = input('enter string : ')#take string as input
opString=''#set null string for output
for i in string:
    if i.isupper():#check whether the character is in uppercase or not
        opString=opString+i.lower()#append charcter by swaping case
    else:#if character is lower case 
        opString=opString+i.upper()#append character by swaping case
print(opString)#print output string