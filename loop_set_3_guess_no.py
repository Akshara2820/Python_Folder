#             GUESSING GAME BNAAOOOO

user=10
while user<=10:
    sum=int(input("guess no. "))
    if user==sum:
        print(sum,"app jeet ghye")
        user=user+sum
    elif user>=sum:
        print(sum,"apka no. CHHOTA  hai ")
    elif user<=sum:
        print(sum,"akpa no. bada  hai ")
    else:
        print("check your no.")
    sum=sum+1





guess=5
n=int(input("enter no."))
while guess!=n:
    if n>guess:
        print("no. bada hai ")
    else:
        print("no. chhota hai")
    n=int(input("enter"))
    print("youu win")
