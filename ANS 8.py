

def fun1(s1):
     s=1
     for i in range(4):
           s*=s1[i]
     print("multiply all the numbers in a list is",s)    
s1=[]
x=int(input(("Enter the limit:")))
for i in range(x):
    n=int(input())
    s1.append(n)
print(s1)    
fun1(s1)    

#=====================================OUTPUT====================================
""" 
Enter the limit:4
34
67
89
65
[34, 67, 89, 65]
multiply all the numbers in a list is 13178230
 """