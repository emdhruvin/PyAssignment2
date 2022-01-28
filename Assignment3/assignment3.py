'''
20CE143 DHRUVIN TANDEL

Mr. Anant is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting K of  members per group where  K ≠ 1.
The Captain was given a separate room, and the rest were given one room per group. Mr. Anant has an unordered list of randomly arranged room entries. 
The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room. Mr. Anant needs 
you to help him find the Captain's room number. The total number of tourists or the total number of groups of families is not known to you. You only know the 
value of K and the room number list.

Input Format
The first line consists of an integer, K , the size of each group.
The second line contains the unordered elements of the room number list.
Constraints: 1< K<1000
Output Format: Output the Captain's room number.
Sample Input
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
Sample Output
8
'''
#SOLUTION
k=int(input('enter number of group : '))#take total number of group
roomList=[int(roomNo) for roomNo in input().split()]#create list with input
check=0#initializig flag 
for i in range(len(roomList)):
    for j in range(len(roomList)):
        if i!=j and roomList[i]==roomList[j]:
            check=1
            break
    if check==0:
        print(roomList[i],end='')#print result
        break
    check=0
