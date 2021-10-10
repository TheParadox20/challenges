def power(x,y):
    omega =x
    for i in range (0,y-1):
        omega*=x
    return omega
print(power(5,3))