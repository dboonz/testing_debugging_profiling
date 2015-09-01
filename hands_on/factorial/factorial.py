""" Compute the factorial of a set of numbers stored in a file. """
import numpy as np

def factorial(n):
    numbers = np.arange(1,n+1).astype(np.float)
    return numbers.prod()

def read_data(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            number = int(line)
            numbers.append(number)
    return numbers


def compute_factorials_for_list(numbers):
    factorials = []
    for number in numbers:
        result = factorial(number)
        factorials.append(result)
    return factorials
    

def main():
    numbers = read_data('numbers.txt')
    factorials = compute_factorials_for_list(numbers)


if __name__ == '__main__':
    main()
