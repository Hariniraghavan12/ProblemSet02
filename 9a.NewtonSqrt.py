#9.a) Write a function NewtonSqrt() to abstract the Newton's Method of calculation Square roots.

def NewtonSqrt(num,iters):
    n=float(num)
    for i in range(iters):
        num=0.5*(num+n/num)
    return num

print(NewtonSqrt(2,100))
