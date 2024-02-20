LUCKY_NUMBER = 67
given_number = int(input('Enter no. between 0 & 100:'))
if given_number == LUCKY_NUMBER:
    print('You guessed correctly!')
elif given_number > LUCKY_NUMBER:  # 87 > 67
    print('Reduce your guessing number')
else:  # given_number < LUCKY_NUMBER
    print('Increase your guessing number')
"""
    Assignment
    ------------------------
    attempts        points
    -----------------------
    1-3             100
    4-9              60
    10-16            20
    17-25             5
    26-               0
"""
attempt = 0
while True:  # do-while loop 
    attempt += 1
    print(f'\n{attempt = }')

    given_number = int(input('Enter no. between 0 & 100:'))
    if given_number == LUCKY_NUMBER:
        if attempt<=3:
           print(f'You guessed correctly! in {attempt} and got 100 points')
        elif attempt>=4 and attempt<=9:
           print(f'You guessed correctly! in {attempt} and got 60 points')
        elif attempt>=10 and attempt<=16:
           print(f'You guessed correctly! in {attempt} and got 20 points')
        elif attempt>=17 and attempt<=25:
           print(f'You guessed correctly! in {attempt} and got 5 points')
        else:
            print(f'You guessed correctly! in {attempt} and got 0 points')
        break
    elif given_number > LUCKY_NUMBER:  # 87 > 67
        print('Reduce your guessing number')
    else:  # given_number < LUCKY_NUMBER
        print('Increase your guessing number')
