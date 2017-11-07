#Task 1

zoo_animals = ["tiger", "lion", "monkey"]

if len(zoo_animals) > 2:
    print('the first animal at the zoo is the ' + zoo_animals[0])
    print('the second animal at the zoo is the ' + zoo_animals[1])
    print('the third animal at the zoo is the ' + zoo_animals[2])

zoo_animals[2] = "deer"
print(zoo_animals)

zoo_animals.append("Peacock")
print(zoo_animals)

start_list = [5, 3, 1, 2, 4]
square_list = []

#Task 2
for x in start_list:
    square_list.append(x ** 2)
square_list.sort()
print(square_list)

#Task 3
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print(menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Italian Pasta'] = 15.00
menu['Nepali Chowmein'] = 20
menu['Hot Pot'] = 25
menu['Momo'] = 30

print("There are " + str(len(menu)) + " items on the menu.")
print(menu)

del menu['Nepali Chowmein']
print(menu)

#Task 4
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket' : ['seashell','strange berry', 'lint']}

inventory['backpack'].sort()
# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['backpack'].remove('dagger')
print(inventory['backpack'])

inventory['gold'] += 50
print(inventory['gold'])

