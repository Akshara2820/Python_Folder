x=int(input("enter no."))
y=int(input("enter no."))
lcm=x*y
while x!=y:
    if x>y:
        x-=y
    else:
        y-=x
lcm=lcm//y
print(lcm)
print(y)
