###################### DAY-1 TASK NO:-1 ##################################

# user = int(input("enter the num:-"))
# a = 1
# while a <= user:
#     if a % 3 == 0 or a % 5 == 0:
#         print(a)
#     a+=1

###################### DAY-1 TASK NO:-2-1 ##################################

# year = int(input("enter the num:-"))

# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print(year,"is a leap year")
#        else:
#            print(year,"is not a leap year")
#    else:
#        print(year,"is a leap year")
# else:
#    print(year,"is not a leap year")

###################### DAY:-1 TASK NO:-2-2 ##################################

# user = int(input("enter the num:--"))
# b=0
# mm=user
# while b < 1:
#     if user % 2 == 0:
        # print("even","\n",mm-2,"\n",mm-4,"\n",mm-6)
        # print("odd","\n",mm+1,"\n",mm+3,"\n",mm+5)
#     else:
        
#         print("even","\n",mm-2,"\n",mm-4,"\n",mm-6)
#         print("odd","\n",mm+2,"\n",mm+4,mm+6)
#     b+=1
        

###################### DAY-1 TASK NO:-2-3 ##################################

# year = int(input("enter the num:--"))

# b=0
# mm=year
# while b < 1:
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print("pichle leap year","\n",mm-4,"\n",mm-8,"\n",mm-12)
#                 print("aane wale leap year","\n",mm+4,"\n",mm+8,"\n",mm+12)
#             else:
#                 print(year,"is not a leap year")
#         else:
#             print("pichle leap year","\n",mm-4,"\n",mm-8,"\n",mm-12)
#             print("aane wale leap year","\n",mm+4,"\n",mm+8,"\n",mm+12)
#     else:
#         print(year,"is not a leap year")
#     b+=1

###################### DAY-1 TASK NO:-3 ##################################

# user = int(input("enter the num:-"))

# user = input("enter the num")
# a=0
# sum=0
# st=str(user)
# for i in st:
#         b=int(i)
#         su=b*b*b
#         sum=sum+su
# if user == sum:
#         print("Armstrong Number")
# else:
#         print("Not Armstrong Number")

##################### DAY-1 TASK NO:-4 ###################################











##################### DAY-1 TASK NO:-5 ##################################









##################### DAY-2 TASK NO:-1 ###################################

# string1=input("enter the str:--")
# m=len(string1)
# if m <= 2:
#     print()
# else:
#     print(string1[:2],string1[-2:])



##################### DAY-2 TASK NO:-2 ###################################

# string1=input("enter you string:---")
# if string1[-3:] == "ing":
#     print(string1+"ly")
# elif string1[-2:]=="ly":
#         print(string1)
# else:
#     if string1[-3:] != "ing":
#         print(string1+"ing")
    
##################### DAY-2 TASK NO:-3 #################################

# string1=input("enter you string:---")
# if string1[-3:] == "ing":
#     m=string1.replace("ing","ly")
#     print(m)
# elif string1[-2:]=="ly":
#         print(string1)
# else:
#     if string1[-3:] != "ing":
#         print(string1+"ing")

##################### DAY-2 TASK NO:-4 #################################

# n=int(input("Enter the num:--"))
# x=0
# y=1
# z=0
# while z <= n:
#     print(z)
#     x=y
#     y=z
#     z=x+y


##################### DAY-2 TASK NO:-5 #################################

# a=1
# sum=0
# n=0
# while a <= 10:
#     m=a*a
#     sum=sum+m
#     n=n+a
#     a+=1
# k=n*n
# l=k-sum
# print(l)

##################### DAY-3 TASK NO:-1 #################################

# user1 = int(input("enter the num:---"))
# a=1
# fac=1
# while a <= user1:
#     fac=fac*a
#     a+=1
# print(fac)

#################### DAY-3 TASK NO:-2 #################################

# user=int(input("enter the num:--"))
# stri=str(user)
# sum=0
# for i in stri:
#     n=int(i)
#     sum=sum+n
# print(sum)

#################### DAY-3 TASK NO:-3 #################################

# user1 = int(input("enter the num:---"))
# sn=str(user1)
# for i in sn:
#     nn=int(i)
#     a=2
#     fac=1
#     sum=0
#     while a <= nn:
#         fac=fac*a
#         sum=sum+fac
#         a+=1
#     print(sum)

#################### DAY-3 TASK NO:-4 #################################

# user = int(input("enter the num:--"))
# sn=str(user)
# pr=sn[::-1]
# m=int(pr)
# print(m)

#################### DAY-3 TASK NO:-5 #################################

# number=2
# power=15
# m=number**power
# qi=str(m)
# sum=0
# for i in qi:
#     nt=int(i)
#     sum=sum+nt
# print(sum)

#################### DAY-4 TASK NO:-1 #################################

# user="Hello app kese ho?"
# ml=user.split(" ")
# count=0
# for i in ml:
#     count+=1
# print(count)

#################### DAY-4 TASK NO:-2 #################################

# dict1 = {"one":1,"two":2,"three":3,"nine":9}
# sum=0
# for i in dict1.values():
#     sum=sum+i
# print(sum)

################################ The End ##################################


8660175105
 
##########

# import json
# employ = ["employ-1","employ-2","employ-3","employ-4","employ-5","employ-6"]
# KEY = ["Name","HomeTown","State","Education","Age","Designation","Sallry"]
# INFO = [
#             ["Pawan","Narwana","Hariyana","12th Pass",22,"Hr",10000],   
#             ["Bhupend","Nagpur","Maharashtra","12th Pass",20,"Treiner",17000,], 
#             ["Amit","Jaunpur","UP","Graguated",24,"Devloper",15000],
#             ["Ranjan","Noida","UP","12th Pass",20,"DataManager",12000],
#             ["Roshan","Nagpur","Maharashtra","Graguated",23,"Facility_Maintence",10000],
#             ["Pratik","Nagpur","Maharashtra","10th Pass",17,"Web_Devloper",30000]
#         ]
# dict1={}
# n=0
# for i in range(len(employ)):
#     dicr = {}
#     for j in range(len(KEY)):
#         dicr[KEY[j]]=INFO[i][j]
#     dict1[employ[i]]=dicr
# # print(dict1)
# k=json.dumps(dict1,indent=4)
# print(k)



# am=['manoj','bipin','nikhil']
# sal=[35000,36000,37000]
# dest=['Delhi','Mumbai','Indore']
# info=['name','salery','destination']
# dict1={}
# dict2={}

# for j in info:
#     dict1[j]=''
# a=1
# list1=[]
# for k in range(len(am)):
#     dict1['name']=am[k]
#     dict1['salery']=sal[k]
#     dict1['destination']=dest[k]
#     list1.append(dict1.copy())
# print(list1)
