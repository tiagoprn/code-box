'''
Given an ordered list, we need to find a number on
that list, in the least amount of guesses possible.
To achieve that, on each guess, we use a number
in the middle of the remaining list, until only one
number remains. If the number is not found, we must
return that.
'''


def binary_search(input_tuple: tuple, number: int):
    attempts = 0
    input_list = list(input_tuple)

    low_index = 0
    high_index = len(input_list) - 1
    # __import__('pudb').set_trace()
    while low_index <= high_index:
        attempts += 1
        print('-' * 80)
        print(f'Attempt number {attempts}...')

        mid_index = int((low_index + high_index) / 2)

        print(f'mid_index: {mid_index}')

        guess = input_tuple[mid_index]
        if guess == number:
            return mid_index

        if guess > number:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1

        print(f'low_index: {low_index }, high_index: {high_index}')

    return None


numbers = input(
    'Enter a list of integer numbers, '
    'separating each one with a space \n'
    '(e.g.: 1, 3, 5, 7, 9 ): '
)

number_to_search = input(
    'Enter an integer number to search on the list \n ' '(e.g.: 999): '
)

numbers_tuple = (int(number) for number in set(numbers.split()))
number = int(number_to_search)

sorted_numbers_tuple = tuple(set(sorted(numbers_tuple)))

print(f'Numbers tuple: {sorted_numbers_tuple}, number to find: {number}')
position = binary_search(sorted_numbers_tuple, number)
if position:
    print(f'Number {number} found at position {position}.')
else:
    print(f'Number {number} NOT found.')
