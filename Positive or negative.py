#Basic if-else questions:
#Write a python program that checks if a number is positive/negative/zero.
a=int(input("enter a value:"))
if a==0:
    print(a,":value is zero")
elif a>0:
        print(a,":value is positive")
elif a<0:
        print(a,":value is negative")
else:
    print("neither positive nor negative")