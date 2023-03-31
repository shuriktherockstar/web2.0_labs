from math import sqrt

def find_perimeter(leg1: int, leg2: int):
    hypotenuse = sqrt(leg1 ** 2 + leg2 ** 2)
    return round(leg1 + leg2 + hypotenuse, 2)

def find_square(leg1: int, leg2: int):
    return round(0.5 * leg1 * leg2, 2)

def main():
    while True:
        try:
            first_leg = int(input('Print first leg: '))
            if first_leg <= 0:
                raise ValueError('Length must be positive')
            second_leg = int(input('Print second leg: '))
            if second_leg <= 0:
                raise ValueError('Length must be positive')
        except ValueError as e:
            print('Incorrect value:', e)
            continue
        print(f'Perimeter = {find_perimeter(first_leg, second_leg)}, square = {find_square(first_leg, second_leg)}')
        break


main()
