import random

def ran_num(): #returns picked by computer number
    return random.choice(range(0,31))

def guess(num):
    i = int(input('Guess the number from 0 to 30: '))
    while i != num:
        if i > num:
            i = int(input('No! My number is smaller. Try another one: '))
        elif i < num:
            i = int(input('No! My number is greater. Try another one: '))
    print('Your are right!')


def main():
    try:
        guess(ran_num())
    except KeyboardInterrupt:
        print('\n')
        print ('See you next time')


if __name__ == '__main__':
    main()
