num=eval(input(' Enter the Number to ciunt Factorial'))
def factorial( num):
    if num==0:
        return 1;
    else:
        return num*factorial(num-1)
n=factorial(num)
print(n)
