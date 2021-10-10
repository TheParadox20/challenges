print('Welcome to the Homework Point Sum progress!')
sum=0
assignments=0
while True:
    score = int(input('Enter a homework score, or -1 to quit: '))
    if (score<0):
        break
    sum+=score
    assignments+=1
print('Homework point sum is ',sum)
if (sum/assignments<33):
    print('Fail')