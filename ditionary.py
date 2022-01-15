# 20CE143 -- DHRUVIN TANDEL
# 
#  A  : check whether the given key is already exist or not 
# person={
#     'fName': 'dhruvin',
#     'lName':'tandel',
#     'age':19,
#     'country':'India'
# }
# flag=0
# givenKey=input('enter key : ')
# for key in person:
#     if givenKey==key:
#         flag=1
#         break
# if flag==1:
#         print(givenKey,' is exist in dictionary person')
# else:
#         print(givenKey,' is not exist in dictionary person')
# 
# B : merge two dictionary
# dic1={ #first dictionay
#     'fName': 'dhruvin',
#     'lName':'tandel',
#     'age':19,
#     'country':'India'
# }
# print('\nfirst dictionary\n')
# for key in dic1:
#     print(key,dic1.get(key))#printing dictoinary
# dic2={#second dictiionary
#     'skills':['photography','coding'],
#     'isMarried':False
# }
# print('\nsecond dictionary\n')
# for key in dic2:
#     print(key,dic2.get(key))
# dic1.update(dic2)  #merge 2 dictionary
# print('\nafter update\n')
# for key in dic1:
#     print(key,dic1.get(key))
# 
# C : sum item in dictionary
# number={
#     '1':1,
#     '2':2,
#     '3':3,
#     '4':4,
#     '5':5
# }
# sum=0
# for key in number:
#     sum+=number.get(key)
# print('sum',sum)
# 
# D :  add key and value to dictionary
# number={
#     '0':10,
#     '1':20,
# }
# check='y'
# while check=='y' or check=='Y':
#     key=input('enter key : ')
#     value=input('enter value : ')
#     number[key]=value
#     print('after adding ',number)
#     check=input('if you want to add more press \'Y\' or press \'N\': ')
#     if check=='n' or check=='N':
#         break 
#
# E : concate dicionary
# dic1={ #dictionary 1
#     1:10,
#     2:10
# }
# dic2={ #dictionary 2
#     3:30,
#     4:40
# }
# dic3={ #dictionary 3
#     5:50,
#     6:60
# }
# #concate in dic1
# print('before cocate\n')
# print('dic1',dic1)#printing dictionaries
# print('dic1',dic2)
# print('dic1',dic3)
# dic1.update(dic2)#concate dictionary 2 in 1
# dic1.update(dic3)#concate dictionary 3 in 1
# print('\nafter concate\n')
# print('dic1',dic1)#print final dictionary