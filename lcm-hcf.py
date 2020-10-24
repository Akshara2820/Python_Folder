# x=int(input("enter no."))
# y=int(input("enter no."))
# lcm=x*y
# while x!=y:
#     if x>y:
#         x-=y
#     else:
#         y-=x
# lcm=lcm//y
# print(lcm)
# print(y)


# n=int(input("enter no."))
# a=1
# c=1
# while 1>0:
#     if a%2!=0:
#         print(a)
#         if c==n:
#             break
#         c+=1
#     a+=1

n=int(input("enter no."))
a=1
if n>1:
    s=2
    while True:
        if n%s==0:
            print("not prime no.")
            if a==n:
                break
            a+=1
        s+=1
    else:
        print("prime no")
else:
    print("not prime no.")
