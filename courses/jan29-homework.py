# Assignment:
# You a list of integers. Write a function in Python to return the frequency of each element in the list.

def numberFrequency(list):
    frequency = {}
    for i in list:
        frequency[i] = frequency[i] + 1 if i in frequency else 1
    return frequency


numbers = [10, 40, 50, 14, 40, 10]
# what will be your turn type?
print(frequency_of_elements(numbers))


def fibbonaci(n):
    if n == 0:
        return 1
    else:
        return n * fibbonaci(n - 1)

print(fibbonaci(5))
