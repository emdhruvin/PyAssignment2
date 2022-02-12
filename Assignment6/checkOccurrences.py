'''
AIM: You are given n words may repeat.
For each word output its number of occurrences.
The output order should corerrespond with the input order of apperence of the word.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample output
3
2 1 1
'''
n=int(input())#take number of total worlds
i=0#index fro loop
word={}#initialize empty dictionary
while i<n:
    str=input()#taking word as input
    if str in  word.keys():#check the word is already exist or not
        word[str]+=1#if yes then increase value by1
    else:
        word[str]=1#if no then keep value as 1
    i+=1
print(len(word))#print the distinct words
i=0
for i in word:
    print(word.get(i),end=" ")#print values stored in dictionary