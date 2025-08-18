from random import randint

print('Welcome to Jazz multiplication challenge')
name=input('Enter your name: ')
ques=int(input(f'Hi {name}, How many questions should I ask you: '))
print('1. Easy')
print('2. Medium')
print('3. Hard')

low_limit=0
high_limit=0
diff=int(input('Please select the difficulty level: '))

if diff==1:
    low_limit=1
    high_limit=10

elif diff==2:
    low_limit=5
    high_limit=10

elif diff==3:
    low_limit=10
    high_limit=20

else:
    print('Rerun the program and enter an integer value from 1-3')
    exit()


right=0
for i in range(1,ques+1):
    a = randint(low_limit, high_limit)
    b = randint(low_limit, high_limit)
    ans = (a * b)
    print('Question ',i,': ',a,' X ',b ,end='', sep='')
    guess=eval(input(' => ').strip())
    if guess==ans:
        print('Right')
        right+=1
    else:
        print('Wrong, the correct answer is',ans)

per_cent= round((right/ques)*100,1)

if right==0:
    print(f'Sorry, you did not get any question right')

elif right<=ques//2:
    print(f'You can do better next time')
    print(f'You got only {right} answers correctly => Percent{per_cent}')


elif (ques//2)<right<ques:
    print(f'Congratulations {name}, you did great!!!')
    print(f'You got {right} answers correctly => Percent: {per_cent}')


else:
    print(f'Congratulations {name}, you did excellently well!!!')
    print(f'You got all answers correctly => Percent: 100')


