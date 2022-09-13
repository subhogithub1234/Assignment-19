""" 
6. Write a python program to create a function that finds a maximum of four numbers.

 """
def fun1(l1):
    print("Maximum number is:{}".format(max(l1)))

x=int(input(("How many number you want to be enter:")))
l1=[]
for i in range(x):
    t=int(input())
    l1.append(t)
fun1(l1)    
#==========================================OUTPUT==============================
"""
 How many number you want to be enter:5
34
67
89
43
79
Maximum number is:89
 """