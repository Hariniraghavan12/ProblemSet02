#method1
bin_no=raw_input("enter a number:")
sum=0
p=0
for i in range(len(bin_no)-1,-1,-1):
    sum=sum+(int(bin_no[i])*(2**p))
    p=p+1
print(sum)
#method2
num=raw_input("enter a number:")
num1=int(num)
sum=0
for i in range(len(num)):
    r=num1%10
    sum=sum+(2**i)*r
    num1=num1/10
print(sum)
