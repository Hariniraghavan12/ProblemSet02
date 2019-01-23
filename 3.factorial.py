def factR(n):
    if(n==1):
        return n
    else:
        return n*factR(n-1)
def factI(n):
    fact=1
    while(n>0):
        fact= fact*n
        n=n-1
    return fact
n=int(input("enter a number:"))
c=raw_input("factorial using Recursion or Iteration:")
c.lower()
if(c=="rec"):
    print(factR(n))
elif(c=="iter"):
    print(factI(n))
else:
    print("enter a valid choice")


