設計一python程式，繪製實心與空心的菱形

#1 實心菱形
n=1
x=11
while n<=11:
   # print("\r"*((11-n)//2)+"*"*n)
    print(("*"*n).center(11,"\r"))
    n+=2
while x>=0:
   # print("\r"*((11-x)//2)+"*"*x)
    print(("*"*x).center(11,"\r"))
    x-=2
print("\n")
 
 
#2 空心菱形
n=1
x=11
while n<=11:
    if n==1:
        print(("*"*n).center(11,"\r"))
    else:
        print("\r"*((11-n)//2)+"*"+"\r"*(n-2)+"*")
    n+=2
while x>=0:
    if x==1:
        print(("*"*x).center(11,"\r"))
    else:
        print("\r"*((11-x)//2)+"*"+"\r"*(x-2)+"*")
    x-=2
