#Task 1
count = 1
if count < 5:
    print(("Hello I am an if statement and the count is"), count)

while count < 5:
    print(("Hello I am a while statement and the count is"), count)
    count += 1

#Task 2
loop_condition = True

while loop_condition:
    print('I am a loop')
    loop_condition = False

#Task 3
num = 1
while num < 11:
    print(num ** 2)
    num += 1

#Task 4
#choice = input('Enjoying the weather (y/n?)')
#while choice != 'y' and choice != 'n':
   # choice = input('Sorry I didnt catch that Please enter again')

#Task 5
count = 0

while True:
    print(count)
    count += 1
    if count >= 10:
        break

#Task 6
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
    print(index, item)
#Task 7
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print(max(a, b))

#Task 8
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')
        break
    print('A', f)
else:
    print('A fine selection of fruits!')
