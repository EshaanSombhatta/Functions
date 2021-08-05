#!/usr/bin/env python
# coding: utf-8


#A1 Write a function to find the maximum and minimum of three numbers.
def maximum(*numbers):
  print("Greatest number =",max(numbers))
maximum(int(input("number one: ")),int(input("number two: ")),int(input("Number three: ")))


#A2 Write a function to reverse an entered string
def reverse(a):
  a=list(a) #turning it into a list so I can use the reverse function
  a.reverse() #using the reverse function
  b=""
  for x in a: #converting to string
    b+=x
  print(b)
reverse(input("Write something: "))



#A3 Write a function that checks whether a passed string is palindrome or not.
def palindromecheck(n):
    b=list(n)
    b.reverse()
    a=list(n)
    if b==a:
        print("It is a palindrome")
    else:
        print("It isn't a palindrome")
palindromecheck(input("Is it a palindrome? "))



#Write a program to execute a string containing Python code.
execute=lambda b:exec(b)
execute(input("input something to write code"))


#A5 Write a function to print the even numbers from a given list.
thelist=[1,234,2,5,24,65,43,32,3,56,6]
print(list(filter(lambda x:x%2==0,thelist)))


#A6 Write a Python function to check whether a number is perfect or not.
#The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 +
#3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 +
#3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the
#perfect numbers 496 and 8128.
def isperfect(n):
    a=0
    for x in range(1,n//2+1):
        if n%x==0:
            a+=x
    if a==n:
        print("number is perfect")
    else:
        print("number isn't perfect")
isperfect(int(input("enter a number to see if it is perfect: ")))


#A7 Write a function to check the given number is prime or not.
def isprime(n):
    a=0
    for x in range(2,n//2+1):
        if n%x==0:
            a+=x
    if a==0:
        print("number is prime")
    else:
        print("number isn't prime")
isprime(int(input("enter a number to see if it is prime: ")))


#A8 Write a function to find factorial of a number using recursion.
def findfactorial(n,a=1):
  a*=n
  if n>1:
    n-=1
    findfactorial(n,a=a)
  else:
    print(a)
findfactorial(int(input("Enter a number to find the number's factorial: ")))


from math import *
def executeoperation(a,b,c):
  d="print("+str(a)+c+str(b)+")"
  exec(d)
a=float(input("Enter a number"))
c=input("enter an operation")
b=float(input("enter another number"))
executeoperation(a,b,c)


from math import pi
def circarea(radius):
    print("circumference =",2*radius*pi)
    print("area =",pi*(radius**2))
circarea(int(input("enter the circle's radius: ")))
