



i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    b=1
    while b<=i:
        print("*",end=" ")
        b+=1
    print()
    i=i+1



i=1
k=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end="")
        b+=1
    j=1
    while j<=k:
        print("*",end="")
        j=j+1
    k=k+2
    print()
    i+=1




row=int(input("enter no."))
for i in range(row):
    print(" "*(row-i)+"* "*(i+1))
for j in range(row-1):
    print(" "*(j+2)+"* "*(row-1-j)) 




row=int(input("enter no."))
index=1
while index<row:
    print(" "*(index-1)+"*",(index+1))
    index=index+1



n=int(input("enter the no."))
k=n
i=0
while i<n:
    a=0
    while a<k:
        print(end=" ")
        a+=1
    k-=1
    j=0
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()



n=int(input("enter the number "))
k = n
i=0
while i<n:
    a=0
    while a<k:
        print(end=" ")
        a+=1
    k-=1
    j=0
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print(" ")


 guess=5
n=int(input("enter no."))
while guess!=n:
    if n>guess:
        print("no. bada hai ")
    else:
        print("no. chhota hai")
    n=int(input("enter"))
    print("youu win")
n=int(input("enter the no."))
k=n
i=0
while i<n:
    a=0
    while a<k:
        print(" ",end="")
        a+=1
    k-=1
    j=0
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()



k=1
i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    b=1
    while b<=i:
        print("*",end=" ")
        b+=1
    print()
    i=i+1

s=1
while s<5:
    m=1
    while m<5-s:
        print(" ",end="")
        s+=1
    n=1
    while n<s:
        print("*",end=" ")
        n+=1
    print()
    s+=1






n=int(input("enter the number "))
k = n
i=0
while i<n:
    a=0
    while a<k:
        print(end=" ")
        a+=1
    k-=1
    j=0
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print(" ")
    

i=1
while i<=5:
    print(" "*(5-i),"*"*i)
    i+=1

i=1
while i<=5:
    j=1
    while j<=5-i:
        print(" "*(5-i),"*"*i)
        i+=1
        
