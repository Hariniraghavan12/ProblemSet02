'''s1=''
list1=[]
def eval_loop(s):
        s1=eval(s)
        list1.append(s1)
while True:
    s=raw_input("enter a string:")
    if(s=='done'):
        print list1.pop()
        break
    else:
        eval_loop(s)'''




s1=''
list1=[]
def eval_loop(s):
    try:
        s1=eval(s)
        list1.append(s1)
    except NameError:
        print("invalid expression")
while True:
    s=raw_input("enter a string:")
    if(s=='done'):
        print list1.pop()
        break
    else:
        eval_loop(s)
