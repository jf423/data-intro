
firstName = input("Enter firstName:")
lastName = input("Enter lastName:")
lengthFirstName = len(firstName)
lengthLastName = len(lastName)

if lengthFirstName == lengthLastName:
    print("Hello " + firstName + " " + lastName)
else:
    if lengthFirstName > lengthLastName:
        print("Hello " + firstName)
    else:
        print("Hello " + lastName)

count = 0
 
for x in "banana":
   count+=1
 
print(count)
