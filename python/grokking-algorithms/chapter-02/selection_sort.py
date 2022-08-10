'''
Selection sort is an algorithm that can be used
when you have to order elements based on some criteria
(in the example below, in ascending order).
You have a list of unordered elements, and
you build a new list where you put the smallest
element at each iteration, until every element
on the unordered list is on the new sorted list.
'''


def find_smallest(array: list):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array: list):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


numbers = input(
    '\nEnter a list of integer numbers to be ordered, '
    'separating each one with a space \n'
    '(e.g.: 1 3 5 7 9 ): '
)

numbers_list = [int(number) for number in numbers.split()]

ordered_list = selection_sort(numbers_list)

ordered_list_as_str = ' '.join(map(str, ordered_list))

print(f'The ordered list is: \n\n {ordered_list_as_str}')
