# without recursion

n1  = int(input('Enter first number: '))
n2  = int(input('Enter second number: '))
n  = int(input('Enter no. of terms: '))

print(n1,n2, end = ' ')
while(n-2):
    c = n1+n2
    n1 = n2
    n2 = c
    print(c, end = ' ')
    n = n-1

# with recursion

def fibonacci(n):
    if n<=1:
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

n = int(input('Enter the no. of terms: '))
for i in range(n):
    print(fibonacci(i), end = ' ')