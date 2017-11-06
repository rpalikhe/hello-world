def tax(bill):
    bill *= 1.08
    print('with tax: %f' % bill)
    return bill
def tip(bill):
    bill *= 1.15
    print('with tip: %f' % bill)
    return  bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


print(("Total amount with tax and tip = %f") % meal_with_tip)

def biggest_number(*args):
    print(max(args))
    return max(args)

def smallest_number(*args):
    print(min(args))
    return min(args)

def distance_from_zero(arg):
    print(abs(arg))
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
