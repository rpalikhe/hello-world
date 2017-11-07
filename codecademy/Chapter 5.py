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

for x in start_list:
    square_list.append(x ** 2)
square_list.sort()
print(square_list)