def findAnEven(l):
    for i in l:
        if(int(i)%2==0):
            return i
        else:
            raise ValueError("there are no even numbers in the list")
num=raw_input("enter the input:")
l=list(num)
print(findAnEven(l))
