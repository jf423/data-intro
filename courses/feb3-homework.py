# Print 10 next numbers starting from a given number using recursion.

def printNextTenWithRecursion(num, count = 1):
    if count == 11:
        return
    print(num)
    printNextTenWithRecursion(num + 1, count + 1)

printNextTenWithRecursion(5)
