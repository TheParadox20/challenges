print('Welcome to the Homework Point Sum program!')
sum=0
assignments=0
while True:
    user_input =input('Do you want to enter a homework score? (\'yes\' or \'no\')')
    if (user_input=='yes'):
        score=int(input('Enter score: '))
        sum+=score
        assignments+=1
    elif (user_input=='no'):
        break
    else:
        print('Unrecognized entry! Please try again.')
print('Homework point sum is ',sum)
if (sum/assignments<33):
    print('Fail')