""" 
10. Write a python program to create a function to check whether a given number is even
or odd.
 """
def fun1(n):
     print("Number is even." if n%2==0 else "Number is odd")
x=int(input("Enter a number:"))     
fun1(x)