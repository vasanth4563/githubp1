# a=(input("enter any word"))
# b=a[::-1]
# if(a==b):
#     print("its a palindrome")
# else:
#     print("its not a palindrome")
import math

# a=int (input("number of a:"))
# b=int (input("number of b:"))
# c=int (input("number of c:"))
# d=int (input("number of d:"))
#
#
# if(a>b and a>c and a>d):
#     print("a is greater")
# elif(b>a and b>c and b>d):
#     print("b is greater-")
# else:
#     print("a is not")





# for i in range(1,5):
#     for j in range(1,5):
#         print(i, end=" ")
#     print()



# rows = 5
#
# for i in range(rows):
#     for j in range(i + 1):
#         numbers=1,4
#         print(numbers,i)





# n=6
# for i in range(1,6):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(n-i):
#         print(i, end=" ")
#     print()
#
# n=6
# for i in range(6):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()



# n=6
# for i in range(6):
#     for j in range(n-i):
#         print("", end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()



# for i in "ABCDE":
#     for j in "ABCDE":
#         print(i,end=" ")
#     print()

#
# fruit=["kiwi","cherry","orange"]
# for x in fruit:
#     print(x)
#
# for x in "orange":
#     print(x)


# for i in range(65,70):
#     for j in range(65,70):
#         print(chr(j),end=" ")
#     print()

#identity
# x=[1,2,3]
# y=[1,2,3]
# z=x
# print(x is y)
# print(z is x)
#
# #membership
# x =("dd","aa","ss")
# print("dd" not in x)



#elif
# a=6
# b=3
# if(a<b):
#     print("hai")
# elif(a!=b):
#     print("hellow")
# elif(a>b):
#     print("bye")


# a=6
# b=3
# if(a>=b):
#     print("hai")
# if(a==b):
#     print("hellow")
# if(a>b):
#     print("bye")
#
#
# a=6
# b=3
# if(a>=b):
#     print("hai")
#     if(a==b):
#         print("hellow")
#     if(a>b):
#         print("bye")
#
#
# a=6
# b=3
# if(a>=b):
#     print("hai")
#     if(a==b):
#         print("hellow")
#         if(a>b):
#             print("bye")

# a=5
# b=6
# if(a>b):
#     pass

# def student():
#     pass

#
# class student:
#     def studentName(self):
#         print("student name is ravi")
#
#     def studentId(self):
#         print("student id is 2202")
#     a="python"
#     print(a.upper())
# obj=student()
# obj.studentName()
# obj.studentId()


# class add():
#     def variable1(self):
#       a=int(input("No1"))
#       b=int(input("No2"))
#       c=a+b
#       return(c)
# class sub():
#     def variable2(self):
#       a=int(input("Num1"))
#       b=int(input("Num2"))
#       c=a-b
#       return(c)
# abj=add()
# print(abj.variable1())
# call=sub()
# call.variable2()


#single inheritance

# class father:
#     f_name="dd"
#     f_age=40
# class son(father):
#     s_name="AA"
#     s_age=10
# s=son()
# print("son name is :",s.s_name)
# print("father name is :",s.f_name)


#multilevel
# class teacher:
#     t_name="swetha"
#     t_age=40
#     t_subject="english"
# class student(teacher):
#     s_name="ram"
#     s_age=30
# class enduser(student):
#     u_name="raj"
#     u_age=35
#
# obb=enduser()
# print("user name is:",obb.u_name)
# print("student age is:",obb.s_age)
# print("teacher subject is:",obb.t_subject)
#
#
# #multiple
# class teacher:
#     t_name="swetha"
#     t_age=40
#     t_subject="english"
# class student():
#     s_name="ram"
#     s_age=30
# class enduser(student,teacher):
#     u_name="raj"
#     u_age=35
#
# obb=enduser()
# print("user name is:",obb.u_name)
# print("student age is:",obb.s_age)
# print("teacher subject is:",obb.t_subject)





# class father:
#     f_name="dd"
#     f_age=40
# class son(father):
#     s_name="AA"
#     s_age=10
#
# class daughter(father):
#     d_name="ss"
#     d_age=12
# s=son()
# print("son name is :",s.s_name)
# print("father name is :",s.f_name)
#
# d=daughter()
# print("father name is :",d.d_name)
# print("father age is :",d.f_age)



#hybrid
# class A:
#     a_name="dd"
#     a_age=40
# class B(A):
#     b_name="AA"
#     b_age=10
#
# class C():
#     c_name="ss"
#     c_age=12
#
# class D(B,C):
#     d_name="jj"
#     d_age=5
#
# obj=D()
# print("b_name is:",obj.b_name)
# print("c_age is:",obj.c_age)
# print("a_name is:",obj.a_name)

#
# import math
# a=math.factorial()
# print(a)


import os
c=os.remove()



