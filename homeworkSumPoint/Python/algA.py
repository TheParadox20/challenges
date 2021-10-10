print('Welcome to the Homework Point Sum progress!')
assignments = int(input('How many assignments did you complete?: '))
sum = 0
for i in range (1,assignments+1):
    print('Enter score ',i,end=': ')
    score = float(input())
    sum += score
print('Homework point sum is ',sum)
if (sum/assignments<33):
    print('Fail')