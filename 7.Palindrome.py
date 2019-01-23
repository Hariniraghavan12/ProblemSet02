import string
def isPalindrome(s):
    str2=''
    for i in range(len(s)-1,-1,-1):
        str2=str2+s[i]
    if(s==str2):
        print("palindrome")
    else:
        print("not a palindrome")
def rem_punct(s):
    s1=''
    for c in s:
        if c in string.punctuation:
            s1=s.replace(c,'')
        return s1
s=raw_input("enter a string:")
s1=rem_punct(s)
isPalindrome(s1)
