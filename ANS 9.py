""" 
9. Write a python program to create a function to check whether a number falls in a
given range.

 """
def fun1(n):
    print("Number is pass." if n>50 and n<100 else "Number is falls.") 
x=int(input(("Enter a number:")))
fun1(x)

#=================================OUTPUT========================================
# Enter a number:45
# Number is falls.