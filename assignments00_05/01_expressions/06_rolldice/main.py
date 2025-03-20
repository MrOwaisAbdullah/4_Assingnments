import random


Num: int = 6

def main():
    dice_1 = random.randint(1, Num)
    dice_2 = random.randint(1, Num)

    total = dice_1 + dice_2

    print(f'\nFirst Die: {dice_1}')
    print(f'Second Die: {dice_2}')
    print(f'\nTotal: {total}\n')

if __name__ == '__main__':
    main()