T = int(input())
maxWeight=0
for i in range (0,T):
    n = int(input())
    a = int(input().split(' '))
    A=[]
    for i in a:
        A.append(int(i))
    A.sort()
    if (n>3):#split into 2 arrays
        weight1 = int(A[len(A)-1])-int(A[0])
        weight2 = int(A[len(A)-2])-int(A[1])
        maxWeight = weight1+weight2
    if (n==2):
        maxWeight = abs(int(A[0])-int(A[1]))
    if (n==3):
        maxWeight = int(A[len(A)-1])-int(A[0])
    print('%i' % maxWeight)
    maxWeight=0