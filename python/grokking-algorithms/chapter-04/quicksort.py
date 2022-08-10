from datetime import datetime


def quicksort(array: list[int], pivot_index_first: bool = True) -> list[int]:
    if len(array) < 2:
        return array  # base case, array is already sorted

    # recursive case:
    if pivot_index_first:
        pivot_index = 0  # first element of the array
    else:
        pivot_index, _ = divmod(len(array), 2)  # middle of the array

    pivot = array[pivot_index]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


numbers = input(
    'Enter a list of integer numbers, '
    'separating each one with a space \n'
    '(e.g.: 1, 3, 5, 7, 9 ): '
)

array = [int(number) for number in set(numbers.split())]

started_at = datetime.now()

sorted_array = quicksort(array, pivot_index_first=False)

finished_at = datetime.now()

took = str(finished_at - started_at)

sorted_array_as_str = ' '.join(map(str, sorted_array))

print(
    f'\nFinished sorting array with quicksort. Took {took}. '
    f'Sorted array: \n\n{sorted_array_as_str}'
)
