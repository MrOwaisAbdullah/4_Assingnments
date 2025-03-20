import random


Num: int = 6

def roll_dice():
    dice_1 = random.randint(1, Num)
    dice_2 = random.randint(1, Num)

    return dice_1, dice_2


def main():
    for _ in range(3):
        dice_1, dice_2 = roll_dice()
        print(f'Die 1: {dice_1}, Die 2: {dice_2}')

if __name__ == '__main__':
    main()