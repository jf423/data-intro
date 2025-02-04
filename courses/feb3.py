# Big O Notation of printBelowTenWithForLoop is O(n) - Linear Time Complexity
def printBelowTenWithForLoop(num):
    for i in range(num, 11):
        print(i)

# Big O Notation of printBelowTenWithRecursive is O(n) - Linear Time Complexity
def printBelowTenWithRecursive(num):
    if num == 10:
        return
    print(num + 1)
    printBelowTenWithRecursive(num +1)

printBelowTenWithRecursive(5)
