####################################### 1-1-1-1-1 ################################################


# a1 = [50, 40, 32, 55, 5, 2, 12]
# a=0
# while a < len(a1):
#     print(a1[a])
#     a+=1


###################################### 2-2-2-2-2 #################################################

# list1=[466,85,6,899,34,26,67,88]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list1):
#         if list1[i]<list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
#         j=j+1
#     i=i+1
# print(list1)
# print(list1[-3:])

#################################### 3-3-3-3-3 ###################################################

# list1 = ["bhupend","praeek","satish","akshay"]
# list2 = [20,93,94,22]
# for i,k in zip(list1,list2):
#     print(i,k)

#################################### 4-4-4-4-4 ##################################################

# lis1 = [1,2,3,4,5]
# new_l=[]

# for i in lis1[::-1]:
#     new_l.append(i)
# print(new_l)

#################################### 5-5-5-5-5 ##################################################

# mylist = [1,2,3,4,5]
# new = [2,3,1,0,5]
# for i in mylist:
#     if i not in new:
#         print(i)

################################### 6-6-6-6-6 ##################################################

# n = [10, 11, 12, 13, 14, 17, 18, 19]
# empty = []
# for i in n:
#     for k in n:
#         m=i+k
#         if m == 30:
#             if [i,k] not in empty and [k,i] not in empty:
#                 empty.append([i,k])
# print(empty)






################################### 7-7-7-7-7 ###################################################

# my_list = [5, 7, 23, 14, 56, 12, 19, 9, 15, 25]









################################### 8-8-8-8-8 ####################################################

# li = [12,32,32,65,77,89]
# sum1 = 0
# for i in li:
#     sum1=sum1+i
# print(sum1)



################################## 9-9-9-9-9 #######################################################

# elements = [23, 14, 56, 12, 19, 9, 15, 25]
# f=len(elements)
# print(f)
# su1=0
# for i in elements:
#     su1=su1+i
# m1=su1/f 
# print(m1)










# my_list = [10, 11, 12, 13, 14, 17, 18, 19]
# empty = []
# for i in my_list:
#     for j in my_list:
#         m=i+j
#         if m == 30 :
#             if ij not in empty and 
#             empty.append([i,j])
# print(empty)



# a=0
# while a < len(my_list):
#     b=0
#     while b < len(my_list):
#         l=my_list[a]+my_list[b]
#         if l == 30:
#             if [my_list[a],my_list[b]] not in empty and [my_list[b],my_list[a]] not in empty:
#                 empty.append([my_list[a],my_list[b]])
#         b+=1
#     a+=1
# print(empty)

##################################11-11-11-11-11##############################################

# my_list = [12,3,12,3,43,45,66,44,12,43,44]
# empty = []
# for i in my_list:
#     if i not in empty:
#         empty.append(i)
# print(empty)

################################## 12-12-12-12 ##################################################

# my_list = [1, [2,3,[3], [245], [2, [4]]]]
# empy = []

# for i in str(my_list[0]):
#     n=int(i)
#     empy.append(n)
#     for j in my_list[1]:
        
        
# print(empy)

#######################################################################################################################################################
#######################################################################################################################################################
#######################################################################################################################################################

# list1 = [1,2,3,4,5,6,7,8,9]

# list2 = ["bhupend","nikhil","rahul","satyam","tushar","raj"]

# dict1 = {}
# new_list1 = []

# lenght1=len(list1)
# lenght2=len(list2)

# if lenght2 == lenght1:
#     for i in range(lenght1):
#         dict1[list1[i]]=list2[i]
#     print(dict1)

# elif lenght1 > lenght2:
#     n1=list1[lenght2:]
#     m1=len(n1)
#     m2=lenght1-m1
#     for i in range(m2):
#         dict1[list1[i]]=list2[i]
#     else:
#         for k in n1:
#             dict1[k]="null"
#     print(dict1)
# else:
#     new_list=list2[lenght1-1:]

#     for i in range(lenght1-1):
#         dict1[list1[i]]=list2[i]
#     dict1[list1[-1]]=new_list
#     print(dict1)

########################## list me se jis list ke length jyada ho uski 





###################################### out put [8,6,4] #######################################################################

# list1=[[1],[2,4,4],[1,2],[4]]
# list2=[]
# a,b,c,d,n=0,0,0,0,0
# while a<len(list1) and c<=n:
#     if type(list1[a])==list:
#         if len(list1[a])>c:
#             b+=list1[a][c]
#         if len(list1[a])>d:
#             d=len(list1[a])
#     if a+1==len(list1):
#         list2.append(b)
#         n,c,a,b=d-1,c+1,0,0
#     a+=1
# print(list2)

############################################################################################################################################

