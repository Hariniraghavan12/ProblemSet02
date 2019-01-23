def is_power(a,b):
    c=a/b
    if((a%b==0) and (c%b==0)):
        return True
    else:
        return False
    
a=int(input("enter first num:"))
b=int(input("enter second num:"))
res=is_power(a,b)
if(res==True):
    print("{} is a power of {}".format(a,b))
else:
    print("{} is not a power of {}".format(a,b))
