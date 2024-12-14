import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-}{][:']"
length_password=int(input("Enter the length of the password:"))
a="".join(random.sample(password,length_password))
#sample extracts some letters from each section used for random sampling without replacement i.e no duplicates
print(f"Your Password is :{a}")
