## Lab - Conditions and Branching

##### 1. There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.

annieYear = 1996
janeYear = 1999
if annieYear%4==0:
    print("Annie is born in a leap year")
elif janeYear%4==0:
    print("Annie is born in a leap year")
else:
    print("none of them born in leap year")

##### 2. In a school canteen, children under the age of 9 are only given milk porridge for breakfast. Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger. The canteen master asks the age of the student and gives them breakfast accordingly. Sam's age is 10. Use if-else statement to determine what the canteen master will offer to him.

sameAge = 10

if sameAge < 9:
    print("given milk porridge")
elif sameAge > 9 and sameAge < 15:
    print("given a sandwich")
elif sameAge > 14 and sameAge < 18:
    print("given a burger")
else:
    print("none")

## Lab - Conditions and Branching

#### Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-4, 5):
    print(i)

# Print the elements of the following list:
# <code>Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']</code>
# Make sure you follow Python conventions.

genres=['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 

for genre in genres:
    print(genre)

# Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']

squares=['red', 'yellow', 'green', 'purple', 'blue']

for square in squares:
    print(square)

# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

playListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

i = 0
rating = playListRatings[i]

while(i < len(playListRatings) and rating > 5):
    i = i + 1
    rating = playListRatings[i]

# Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

# Write your code below and press Shift+Enter to execute

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while(i < len(squares) and squares[i] == 'orange'):
    i = i + 1
    new_squares.append('orange')
print (new_squares)

# Your little brother has just learned multiplication tables in school. Today he has learned tables of 6 and 7. Help him memorise both the tables by printing them using for loop.

for i in range(1, 11):
    print("6 *",i,"=", 6*i)
for j in range(1, 11):
    print("7 *",j,"=", 7*j)

# The following is a list of animals in a National Zoo. Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
# Your brother needs to write an essay on the animals whose names are made of 7 letters. Help him find those animals through a while loop and create a separate list of such animals.

animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
animalSeven = []
i = 0

while(i < len(animals)):
    if len(animals[i]) == 7:
        animalSeven.append(animals[i])
    i = i + 1

print(animalSeven)
