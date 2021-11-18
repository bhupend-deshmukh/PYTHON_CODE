
################################# fibunaci serice ##########################################

# n=int(input("Enter the num:--"))
# x=0
# y=1
# z=0
# while z <= n:
#     print(z)
#     x=y
#     y=z
#     z=x+y


#############################################################################################################
#############################################################################################################
#####################################!! STRING IN PYTHON !!######################################################
#############################################################################################################
#############################################################################################################

######################################## 100 time name print without lool ###############################################

# print(100*("bhupendra\n"))

######################################## vahi question 1 line new leke #########################################

# print(100*("\nbhupendra\n"))

######################################## output /\/\/\/\/\/\/\/\/\/\ #######################################

# print(5*"/\\")
# print("/\/\/\/\/\\")

######################################## reverse kre list ke eliment ko ###################################

# a=["rahul","suraj","nasir"]
# new_list=[]
# for i in a:
#     m=i[::-1]
#     new_list.append(m)
# print(new_list)

################################################ sat lana hai out put me #########################################

# string = "['s','a','t']"
# m=string.strip(",")
# vl=""
# for i in m:
#     v=i.strip("',")
#     for k in v: 
#         vl=vl+k
# mn=vl.strip("[]")
# print(mn)

################################################ 2 string ko milana ha #################################################

# a="satyam1123"
# b="kumar"
# c=""

# b1=len(b)
# a1=len(a) 

# if a1>b1:
#     s=a[:b1]
#     bc=a[b1:]
#     print(s)
#     print(bc)

#     for i,m in zip(s,b):
#         c=c+i+m
#     print(c+bc)
# elif b1 > a1:
#     k=a[:b1]
#     bnc=a[b1:]
#     print(k)
#     print(bnc)
#     for i,m in zip(k,b):
#         c=c+i+m
#     print(c+bnc)

##################################### factorial number ###############################################

# user = int(input("enter the num:---"))
# a=1
# fact=1
# while user > 0:
#     fact=fact*user 
#     user-=1
# print(fact)


# user1 = int(input("enter the num:---"))
# a=1
# fac=1
# while a <= user1:
#     fac=fac*a
#     a+=1
# print(fac)

#################################### Prime Number ######################################################


# a=int(input("enter the num:--"))
# b=1
# count=0
# while b <= a:
#     if a % b == 0:
#         count+=1
#     b+=1
# else:
#     if count == 2:
#         print("its prime number!!!!!")
#     else:
#         print("its not prime number!!!!!!!")


#################################### Prime Number ######################################################


# a=10
# b=a=-2
# print(b)


# mn=a[:-1]
# print(mn)
# for k in a:
#     print(k)


# for i,m in zip(a,b):
#     c=c+i+m
# print(c)

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[:5])  

# b = "Hello, World!"
# print(b[2:])

# b = "Hello, World!"
# print(b[-5:-2])

# list1 = [1,2,77,3,4,99,5,66]
# dn=[]
# for j in list1:
#     for k in list1:
#         if j < k:
#             dn.append(j)
# print(dn)

# txt = "hello, and welcome to my world."

# x = txt.capitalize()

# print (x)






########################################################################################################################################################
########################################################################################################################################################

import json

# # name=input("emter the name:--")
# # email=input("enthe the email address:--")
# # mo_num=int(input("enter the num:--"))
# # mk=open("data.json","r")
# # l=mk.read()
# # print(l)

# # dict1 = {}
# # list1=[]
# # dict1["name"]=name
# # dict1["email"]=email
# # dict1["contact"]=mo_num
# # list1.append(dict1)

# # n=open("data.json","a")
# # m1=json.dump(list1,n,indent=4)
# # print(m1)

# name=input("emter the name:--")
# email=input("enthe the email address:--")
# password=input("enter the password:---")
# mo_num=input("enter you mobile number...")

# dict1 = {}
# dict2 = {}
# list1 = []

# dict1 = {}
# list1=[]
# dict1["name"]=name
# dict1["email"]=email
# dict1["password"]=password
# dict2[mo_num]=dict1
# # dict1["contact"]=mo_num
# list1.append(dict2)



# # with open("data.json","w") as l:
# #     json.dump(list1,l,indent=4)


# print("""
#     1) add

#     2) update

#     3) delete
#     """)
# use=int(input("enter the num:--"))
# if use == 1:
#     with open("data.json","r") as n:
#         g=json.load(n)
#         listq = []
#         for i in g:
#             for j in i.keys():
        
#                 listq.append(j)
#         g.append(dict2)
#         for n in dict2.keys():
#             print(n)
#             if n in listq:
#                 print("yh data allredy available hai")
#                 print("sorry please aap new add kijiye ")
#                 user=1
#                 if user == 1:

#             else:
#                 with open("data.json","w") as b:
#                     json.dump(g,b,indent=4)
# elif use == 2:
#     with open("data.json","r") as n:
#         g=json.load(n)
     
     
     ###########################################################################
     
     
     V
# # # a=[1,2,3,[4,5],6,7]
# # # i=0
# # # list1=[]
# # # while i<len(a):
# # #     if type(a[i])!=list:
# # #         list1.append(a[i])
# # #     else:
# # #         b=0
# # #         while b<len(a[i]):
# # #             if type(a[i])==list:
# # #                 list1.append(a[i][b])
# # #             b=b+1
# # #     i=i+1
# # # print(list1)

# # # list1 = [1,2,3,4,5,6,7,8,9]
# # # even=[]
# # # odd=[]
# # # prime=[]
# # # for i in range(len(list1)):
# # #     if list1[i] % 2 == 0:
# # #         even.append(list1[i])
# # #     if list1[i] % 2 != 0:
# # #         odd.append(list1[i])
# # #     m=1
# # #     count=0
# # #     while m <= list1[i]:
# # #         if list1[i] % m == 0:
# # #             count+=1
# # #         m+=1
# # #     else:
# # #         if count == 2:
# # #             prime.append(list1[i])
# # # print('even')
# # # for j in even:
# # #     print(j)
# # # print('odd')
# # # for l in odd:
# # #     print(l)
# # # print("prime")
# # # for m in prime:
# # #     print(m)




# # list= [1,2,3,4,5,6,7,8,9]
# # even=[]
# # odd=[]
# # prime=[]
# # for i in range(len(list)):
# #     if list[i] % 2 == 0:
# #         even.append(list[i])
# #     if list[i] % 2 != 0:
# #         odd.append(list[i])
# #     m=1
# #     count=0
# #     while m <= list[i]:
# #         if list[i] % m == 0:
# #             count+=1
# #         m+=1
# #     else:
# #         if count == 2:
# #             prime.append(list[i])
# # print(even)
# # print(odd)
# # print(prime)   

