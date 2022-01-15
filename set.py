#20CE143 -- DHRUVIN TANDEL
#A : add members in set and clear it
# s1={1,2,3,4,5}
# check='y'
# while check == 'y' or check == 'Y':
#     num=input('enter a number : ')
#     s1.add(num)
#     print(s1)
#     check=input('press \'d\'. for delete number \n\'y\'.for add number\n\'n\'. for exit\n : ')
#     if check=='n' or check =='N':
#         break
#     if check=='d' or check=='D':
#         s1.clear()
#         print(s1)
# 
#B :  remove item from set if it is present
# s1={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# check='y'
# flag=0
# while check=='y' or check=='Y':
#     ele=int(input('enter element you want to remove : '))
#     for i in s1:
#         if i==ele:
#             s1.remove(ele)
#             flag=1
#             print('after remove ',s1)
#             break
#     if flag==0:
#         print('element does not exist...')
#     check=input('\nenter \'y\'.for remove element \n\'n\'.for exit \n : ')
#     if check=='n' or check =='N':
#         print(s1)
#         break
# 
#C : intersection and union
# set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set2 = {0, 2, 4, 6, 8, 10, 12, 14}
# set3 = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# set4 = {1, 3, 5, 7, 9, 11}
# print('Intersection of', set1, 'And', set2, 'is:- ', set1.intersection(set2))
# print('Union of', set1, 'And', set3, 'is:- ', set1.union(set3))
# print('Difference of', set1, 'From', set4, 'is:- ', set1.difference(set4))
# 
#D : find MAX and MIN 
# set1 = {-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# MAX = 0
# MIN = 0
# for item in set1:
#     if item > MAX:
#         MAX = item
#     elif item < MIN:
#         MIN = item

# print('Maximum value in a set is:- ', MAX)
# print('Minimum value in a set is:- ', MIN)
#
#E :  count
print('For List:- ')
lst = [1, 1, 2, 3, 4, 1, 4, 2, 4, 5]
value = 0
count = {}
for item in lst:
    for item2 in lst:
        if item2 == item:
            value = value + 1
            count[item] = value
    value = 0
for key in count:
    print('\tElement:-', key, '\tCount:-', count.get(key))

print('\nFor Tuple:- ')
tuple1 = ('Python', 'C', 'C++', 'C', 'Java', 'C', 'Python')
value = 0
count = {}
for item in tuple1:
    for item2 in tuple1:
        if item2 == item:
            value = value + 1
            count[item] = value
    value = 0
for key in count:
    print('\tElement:-', key, '\tCount:-', count.get(key))

print('\nFor Dictionary:- ')
Dictionary = {
    'Player 1': 'Ketan',
    'Player 2': 'Dhruvin',
    'Player 3': 'Pratik',
    'Player 4': 'Pratham',
    'Player 5': 'Pratik',
    'Player 6': 'Pratham'
}
value = 0
count = {}
for key in Dictionary:
    for key2 in Dictionary:
        if Dictionary.get(key2) == Dictionary.get(key):
            value = value + 1
            count[Dictionary.get(key)] = value
    value = 0
for key in count:
    print('\tElement:-', key, '\tCount:-', count.get(key))