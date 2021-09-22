n = int(input('Enter a positive number: \n'))
while 1:
    print(n)
    if (n<0):
        print('Not a positive number. Exiting.')
        break
    elif n==1:
        break
    if n%2==0:
        n /=2
    elif n%2!=0:
        n = 3*n+1