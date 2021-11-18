# for i in range(5,0,-1):
#     print(5*f"{i}")


###################################### Table Print #####################################

# user=int(input("enter the num:-"))
# for i in range(1,11):
#     print(user,"x",i,"=",user*i)

######################################







# import requests,json
# f=requests.get("http://saral.navgurukul.org/api/courses").text
# data=json.loads(f)
# a=0
# id=[]
# for i in data['availableCourses']:
#     print(str(a)+"} "+i['name'])
#     id.append(i['id'])
#     a+=1
# user=int(input('enter course nuumber:  '))
# slug=requests.get('http://saral.navgurukul.org/api/courses/'+id[user]+'/exercises').text
# print('http://saral.navgurukul.org/api/courses/'+id[user]+'/exercises')
# data1=json.loads(slug)
# b=1
# c=1
# for i in data1['data']:
#     print(str(b)+"]  "+i['name'])
#     child=i['childExercises']
#     for i in child:
#         print("        "+str(b)+"."+str(c)+i['name'])
#         c+=1
    # b+=1





###############################################################################################################################
###############################################################################################################################
#------------------- 1 to 100 bitween prime number ----------------------------------------------------------------------------
################################################################################################################################
################################################################################################################################



# for i in range(100):
#     m=1
#     count=0
#     while m <= i:
       
#         if i % m == 0:
#             count+=1
#         m+=1
#     else:
#         if count == 2:
#             print(i,'prime number')


##################################################################################################################################
####################################################################################################################################
###################################################################################################################################

# for i in range(10):
#     m=1
#     count=0
#     while m <= i:
#         if i % m == 0:
#             count+=1
#         m+=1
#     else:
#         if count == 2:
#             print(i,'prime number !!!!!')




# n=50000
# x=0
# y=1
# z=0

# user1=int(input("enter the num :----"))
# user2=int(input('enter the number :----'))

# list1=[]
# u=0
# while True:
#     u+=1
#     print(z)
#     if z > 0:
#         if z % user1 == 0:
#             list1.append(z)
#     if len(list1) == user2:
#         break

#     x=y
#     y=z
#     z=x+y

# print(list1[-1])
# print(u,'all index in divisible by')
    
# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# new1=[]

# for j in n:
#     for k in n:
#         m=k+j
#         if m == 30:
#             if [j,k] not in new1 and [k,j] not in new1:
#                 new1.append([j,k])
# print(new1)

# from _typeshed import StrPath
# from os import spawnl


# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]

# row=[]
# row2=0
# row3=0

# colum1=[]
# colum2=[]
# colum3=[]

# diag1=0
# diag2=0
# string=''

# for i in range(len(magic_square)):
#     mm=0


#     for j in magic_square[i]:
#         mm+=j
#     colum1.append(mm)
    # for k in magic_square:


    # if a<1:
    #     b=0
    #     c=2
    #     for l in magic_square:
    #         diag1+=l[b]

    #         b+=1
    #         a+=1
    #         diag2+=l[c]
    #         c-=1

    

#     for j in magic_square[i]:
#         print


# import json
# listi=[]
# employ=['emp1','emp2','emp3']
# detail=['Name','Education','Work','Sallry']
# other=[
#             ['Nasir','12th Pass','Web Developer',10000],
#             ['Roshan','garaduate','python developer',25000],
#             ['Satish',"12th Pass",'bacend Devloper',20000],
#             ['Bhupendra','12th pass','Frountend Developer',20000]
#         ]

# dict1 = {}
# dict3={}
# a=0
# while a < len(employ):
#     b=0
#     while b < len(detail):
#         dict1[detail[b]]=other[a][b]
#         b+=1
#     dict3[employ[a]]=dict1
#     a+=1
# listi.append(dict3)
# with open('l
# import json
# listi=[]
# employ=['emp1','emp2','emp3']
# detail=['Name','Education','Work','Sallry']
# other=[
#             ['Nasir','12th Pass','Web Developer',10000],
#             ['Roshan','garaduate','python developer',25000],
#             ['Satish',"12th Pass",'bacend Devloper',20000],
#             ['Bhupendra','12th pass','Frountend Developer',20000]
#         ]

# dict1 = {}
# dict3={}
# a=0
# while a < len(employ):
#     b=0
#     while b < len(detail):
#         dict1
# import json
# listi=[]
# employ=['emp1','emp2','emp3']
# detail=['Name','Education','Work','Sallry']
# other=[
#             ['Nasir','12th Pass','Web Developer',10000],
#             ['Roshan','garaduate','python developer',25000],
#             ['Satish',"12th Pass",'bacend Devloper',20000],
#             ['Bhupendra','12th pass','Frountend Developer',20000]
#         ]

# dict1 = {}
# dict3={}
# a=0
# while a < len(employ):
#     b=0
#     while b < len(detail):
#         dict1[detail[b]]=other[a][b]
#         b+=1
#     dict3[employ[a]]=dict1
#     a+=1
# listi.append(dict3)
# with open('lastdata.json','w') as l:
#     json.dump(listi,l,indent=4)
#     print('Done')[detail[b]]=other[a][b]
#         b+=1
#     dict3[employ[a]]=dict1
#     a+=1
# listi.append(dict3)
# with open('lastdata.json','w') as l:
#     json.dump(listi,l,indent=4)
#     print('Done')astdata.json','w') as l:
#     json.dump(listi,l,indent=4)
#     print('Done')

#-------------------------------------------------------------------------------




        