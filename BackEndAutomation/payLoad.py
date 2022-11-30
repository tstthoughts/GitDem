def addBookPayload(isbn):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "227",
        "author": "John foe"
    }
    return body


games = ['tennis', 'baseball', 'rugby', 'soccer']
i = 0

while i < len(games):
    print(games[i])
    i += 1



numList = [1,2,3]
for n in numList:
    print(n**2)

num1 =15
num2 =16
sum = num1 + num2
print("sum of {0} and {1} is {2}".format(num1, num2,sum))
print("sum:", num1 + num2)

for x in range(1, 5):
    print(x),

gamess = ['tennis', 'baseball', 'rugby', 'soccer']
iterator = iter(gamess)

# we use the next() function to
# print the next item of iterable
print(next(iterator))

n1 = input("user input 1: ")
print(n1)


# creating our own loop
def newForLoop(iterable):
    # extracting iterator out of iterable
    iterator = iter(iterable)

    # condition to check if looping is done
    loopingFinished = False

    while not loopingFinished:
        try:
            nextItem = next(iterator)
        except StopIteration:
            loopingFinished = True
        else:
            print(nextItem)

        # Driver's code


newForLoop([1, 2, 3, 4])
A = {1,2,3}
B = {2,3}
print (A.difference(B))
