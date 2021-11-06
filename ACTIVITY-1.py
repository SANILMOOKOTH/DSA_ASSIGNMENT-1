#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
side=float(input("Enter the side of the equilateral triange: "))
area = ((math.sqrt(3))/4)*(math.pow(side,2))
print('Area=' , area)


# # Write a program to count the number of each character in a string

# In[2]:


string=input('enter the string')
for i in string:
    print(i,"=",string.count(i))


# # Write a program to find the area and perimeter of a rectangle using functions

# In[3]:


l=int(input("length :"))
w=int(input("width :"))
area=l*w
perimeter=2*(l+w)
print('Area of a rectangle :',area)
print('perimeter of a rectangle :', perimeter)


# # Write a program to print the fibonacci series till a specified number

# In[8]:


n=int(input("Enter the value of'n' "))
a=0
b=1
sum=0
count=1
print('fibinocci series:', end=" ")
while( count<=n):
    print(sum, end =' ')
    count+=1
    a=b
    b=sum
    sum=a+b


# # Complete the following code to find the minimum of 3 number using conditional statements.Output should be as displayed

# In[ ]:





# In[4]:


a,b,c =input ('Enter three number followed by:').split()
print("First Number:", a)
print("Second Number:", b)
print("Third Number:", c)
if(a==b==c):
    print("Entered numbers are equal")
else:
    if(a<b and a<c):
        print(a, "is the smallest number")
    elif b<c:
        print(b, "is the smallest number")
    else:
        print(c, "is the smallest number")    


# # Write a program to print star pyramid.The number of rows should be taken as input from the user

# In[28]:


r=int(input("Enter number of rows:"))
V=number-1
for i in range(0,r):
    for j in range(0,v):
    v-=1
     for j in range(0,i+1):
         print("*",end="")
        print('\r')


   


# # Complete the following code to convert hour into seconds

# In[24]:


def to_seconds(t):
    s=t*3600
    return s
time_in_Hours=int(input("Enter time in Hours"))
print(time_in_Hours,"Hour is equal to",to_seconds(time_in_Hours), "seconds")


# In[ ]:





# # Write a program to print multiplication table as below

# In[23]:


number=int(input("Enter a number to find the multiplication table:" ))
for i in range(1,11):
    print(i,"x",number,"=",i*number)


# # write a program to take your favourite food as list and print each as "I like Biriyani"

# In[22]:


a,b,c = input("enter your favourite food list :").split()
print( "I like ",a)
print( "I like ",b)
print( "I like ",c)


# In[ ]:




