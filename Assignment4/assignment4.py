'''
20CE143 DHRUVIN TANDEL

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.

Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.

Output Format: Print the runner-up score.

Sample Input
5
2 3 6 6 5
Sample Output
5
'''
n=int(input())#take input of number of participate
score= list(map(int, input().strip().split()))[:n]#list that store score of participate
score.sort()#sort list
i=n-1#initialize counter
while(score[i]==score[i-1] and i>=0):
    i-=1
print(score[i-1])#print result