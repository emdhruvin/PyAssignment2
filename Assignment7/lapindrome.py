'''
AIM:Lapindrome is define as a string which when split in the middle give two halves having the same 
characters and same frequency of each character in the string. 
If there are odd number of number of characters in string we ignore the middle character and check for lapindrome.
For example gaga is a lapindrome string since the two halves ga and ga have the same characters with same frequency.
Also abccba, rotor and xyzxy are lapindrome.
Note that abbaab is not a lapalindrome. the two halves contain same characters but their frequency does not match


Sample Input
6
gaga
abcde
rotor
xyzxy
abbaab
abcabc

Sample Output
YES
NO
YES
YES
NO
NO
'''
n=int(input())#take input fro total input
while n:#loop will continue until n is become 0
    str=input()#take word as input
    half=len(str)//2#store floor value by dividing the length by 2
    if len(str)%2==0:#check string is of even length or not
        if sorted(str[:half])==sorted(str[half:]):#check sorted of before half and after half are same or not
            print('YES')#if yes then print YES
        else:
            print('NO')#if no then print NO
    else:#if string is of odd length
        if sorted(str[:half]) ==sorted(str[half+1:]):#check sorted of before half and after half are same or not
            print('YES')#if yes then print YES
        else:
            print('NO')#if yes then print NO
    n-=1