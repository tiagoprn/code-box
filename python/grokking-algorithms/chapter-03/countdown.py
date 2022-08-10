'''
That is a simple example of a recursive function.

Every recursive function has 2 parts:
    - base case: the condition to stop the recursivity.
    - recursive case: when the function calls itself.
'''


def countdown(i: int):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


number = input(
    'Enter an integer number to start the countdown with\n ' '(e.g.: 9): '
)

countdown(int(number))
