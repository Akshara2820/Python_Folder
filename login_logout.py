        #    login logout code





name=input("enter the username ")
password=input("enter the password ")
if name>="a" or name>="A":
	if  len(password)==8 and '@' in  password or '#' in password or '%' in password:
		print("secessfull login")
		l=input("\t tap 1 no. for logout")
		if l=="1":
			print("You logout")
	else:
		print("password is not strong")
else:
	print("username is somethng wrong")