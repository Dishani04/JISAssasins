#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 Write A program to accept  Four digit number from user and count zero , odd and even digits from the entered number.
class Count:
    def counting(self,num):
        x=num
        i=0
        e=0
        o=0
        z=1
        count=4
        while(count>0):
            z=x%10
            if z==0:
                i+=1
            elif z%2==0:
                e+=1
            elif z%2 !=0:
                o+=1
            x=x//10
            count-=1
        print("Zeroes={},Evens={}, Odds={}".format(i,e,o))
        
c=Count()
num=int(input("Enter a four digit number:"))
c.counting(num)


# In[2]:


# 2 Write a   program to accept ‘n’ numbers from user , store these numbers into an array. Find out maximum and minimum number from an Array.
class MaxMin:
    def MaxandMin(self,list):
        z=min(list)
        y=max(list)
        print("{} is minimum and {} is maximum".format(z,y))
        
m=MaxMin()
list=[]
n=int(input("Enter how many numbers to input:"))
while(n>0):
    a=int(input())
    list.append(a)
    n-=1
m.MaxandMin(list)


# In[ ]:





# In[5]:


# 9 Write a program to calculate the sum of first digit and last digit of a given number
n = int(input("ENTER THE NUMBER :"))

rev = 0
fd = 0
s = 0

ld = n % 10

while n > 0:
    r = n % 10

    rev = rev * 10 + r

    n = int(n / 10)

fd = rev % 10

s = fd + ld

print("SUM OF THE 1ST DIGIT NO AND LAST DIGIT NO IS :", s)


# In[ ]:


#Ques:10 Write a program to accept a string from user , delete all vowels from the string and display the result.

string=input("enter the string: \n")
rem_vowel(string)
def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
    print(string) 


# In[15]:


# 16 Write a Program to Accept character and display its Ascii value and its Next and Previous Character. 
class Letr:
    def Ascii(self,c):
        
        y=ord(c)
        nex=chr(ord(c)+1)
        pre=chr(ord(c)-1)
        print("{}={} next letter={} prev letter ={}".format(c,y,nex,pre))
l=Letr()
c=input("enter c\t")
l.Ascii(c)


# In[16]:


# 15 Write a program to calculate  X(Y+Z) .
x=int(input("enter a value"))
y=int(input("enter another number"))
z=int(input("enter 3rd number"))
a=y+z
print("the result is",x**a)


# In[ ]:


# 14 Write a program to accept ‘n’ numbers from user and store these numbers into an array and count the number of occurrences of each number.
def countX(lst, x): 
    return lst.count(x) 
q=input("enter the number:")
lst=q.split(" ")
x = '9'
print(countX(lst, x)) 


# In[1]:


# 12 Write a  program to accept a sentence from the user and reverse its each word.
def reverseWordSentence(Sentence): 
 
    return ' '.join(word[::-1]
                    for word in Sentence.split(" ")) 
  

Sentence = input("enter the string \n")
print(reverseWordSentence(Sentence))     


# In[6]:


# 8 Write a program to swap the values of two variables using Call by Reference.

class Swap:
    def swapping(self,x,y):
        temp=x
        x=y
        y=temp
        print("after swapping the value will be:",x,y)
s=Swap()
x=int(input("enter a number"))
y=int(input("enter a another number"))
s.swapping(x,y)


# 

# In[3]:


# 7 Write a program to calculate the sum of digits of a given number.
class Sum:
    def sumation(self,num):
        num1=num
        add=0
        
        while num>0:
            num1=num%10
            add+=num1
            num=num//10
        print("the addition is",add)
            
        
c=Sum()
num=int(input("Enter a number:"))
c.sumation(num)


# In[9]:


# 18 Write a program to calculate the x to the power y without using Standard functions
num=int(input("enter a number"))
num2=int(input("enter 2nd number"))
a=1
for num2 in range (1,num2+1):
    a=(a*num)
print(a)


# In[10]:


# 13 Write a program to calculate sum of elements of M*N matrix.
matrix1 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
matrix2 = [[10,11,12],
          [13,14,15],
          [16,17,18]]
rmatrix = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]
for r in rmatrix:
    print(r)


# In[12]:


# 6 Write a program to accept 5 names from user and store these names into an array sort these array element in alphabetical order.
names=[]
n=5
for x in range(1,n+1,1):
    names.append(input("Enter the names:"))
names.sort()
print("Names after sorting are",names)


# In[1]:


#Ques:11 Write a program to accept a string value from the user and accept a char value from the user and and find out the total occurrence of char value in the string value.

str=input("Enter the string \n")
char=input("Enter the character whose number of occurences is to be found in the string \n")
c=str.count(char)
print("Number of occurences of {} is {}".format(char,c))


# In[2]:


# question 4
n=int(input("Enter number of inputs:"))
arr=[]
brr=[]
i=0
j=0
while(n>0):
    a=int(input())
    arr.append(a)
    n-=1
print(arr)
arr.sort()
print(arr)


# In[4]:


# question 3
database = {}
z=True
while(z):
    class Library:
        print("------MENU-----")
        print("1.ADD BOOK INFORMATION\n2.DISPLAY BOOK INFORMATION\n3.LIST ALL BOOKS OF GIVEN AUTHOR \n4.LIST THE COUNT OF BOOKS IN THE LIBRARY \n5.EXIT") 

        def inputdata(self,author,book):
            database[book]=author
            print("add complete")
        def display(self):
            print(*database)
        def liststep(self,author):
            def fill(n):
                if database[n]==author:
                    return True
                else:
                    return False
            res=filter(fill,database)
            for i in res:
                print(i)
        def countbook(self):
            print("total number of book present in library is ",len(database.keys()))

    l=Library()
    ch=input("Enter your choice:\n")
    if ch=='1':
        a=input("Enter the name of autnhor:\n")
        b=input("Enter the book name:\n")
        l.inputdata(a,b)
    elif ch=='2':
        l.display()
    elif ch=='3':
        aut=input("Enter the name of author to list books:\n")
        l.liststep(aut)
    elif ch=='4':
        l.countbook()
    else:
        print("thaks")
    k=input("do want to enter a number(y/n):\n")
    if k!="y":
        z=False


# In[ ]:




