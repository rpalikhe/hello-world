#Task 1
n = [1,2,3,4,5]
n[1] = n[1]*5
n.append(6)
n.pop(0)
print(n)

#Task 2
n = 'Hello'
m = [5,6,9]
def string_function(s):
    return s + ' world'
string_function(n)
print(string_function(n))

def list_function(z):
    return z
print(list_function(m))

#Task 3
def list_function1(x):
    x[1]= x[1] + 3
    return x
n = [9, 10,15]
print(list_function1(n))

#Task 4
def double_first(n):
    n[0] = n[0] * 2
numbers = [9,8,7,6,4]
double_first(numbers)
print(numbers)

#Task 5
n = [1,2,3,4,5]
def print_list(x):
    for i in range(0, len(x)):
        print(x[i])
print(print_list(n))

#Task 6
n = [5,7,9,10]
def double_num(k):
    for i in range(0, len(k)):
        k[i] = k[i] * 2
    return k
print(double_num(n))

#Task 7

def new(p):
    for i in range(0, len(p)):
        p[i] = p[i] * 2
    return p
print(new(list(range(5))))

#Task 8
n = [10,5,7]

def total(numbers):
    result = 0
    for i in (list(range(0,len(numbers)))):
        result += numbers[i]
    return result
print(total(n))

#Task 9
w = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in words:
        result += i + " "
    return result

print(join_strings(w))

#Task 10
list_of_lists = [[1,2,3],[4,5,6]]
for x in list_of_lists:
    print(x)
    for y in x:
        print(y)
