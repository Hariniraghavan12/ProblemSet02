sum=0
def sumDigits(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            sum=sum+int(s[i])
    return sum
s=raw_input("enter an alpha-numeric string:")
try:
    ans=sumDigits(s)
    print(ans)
except Exception:
    print("enter a valid alpha-numeric string")
