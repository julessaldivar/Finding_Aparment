def apt_search1(city, min_beds, max_rent, pets_allowed=True):  # defining function
    if pets_allowed:
        return (f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds}\n'  # runs when true
                f'bedroom apartments that allow pets, all within the budget of ${max_rent} per month.')
    else:
        return (f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds}\n'
                f'bedroom apartments, all within the budget of ${max_rent} per month.')  # runs when pets allowed false


print(apt_search1('Grand Rapids', 2, 1800, True), '\n\n')  # using function


def apt_search2(city: str, max_rent: int, min_beds: int = 0, pets_allowed: bool = True):  # indicated each data type
    if pets_allowed:
        return (f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds}\n'  # runs when true
                f'bedroom apartments, all within the budget of ${max_rent} per month.')
    else:
        return (f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds}\n'  # runs when false
                f'bedroom apartments that allow pets, all within the budget of ${max_rent} per month.')


print(apt_search2('Grand Rapids', 1800), '\n\n')  # calling with min_beds and pets_allowed omitted

print(apt_search2('Grand Rapids', 1800, 3), '\n\n')  # calling with just min_beds and no pets_allowed

print(apt_search2('Grand Rapids', 1800, int(), False), '\n\n')  # calling with just pets_allowed, no min_bed

plus_one_hundred = lambda x : x + 100  # Using Lambda adding 100 to any given number
print(plus_one_hundred(15))            # 115

square_num = lambda x : x ** 2  # Using Lambda to square any given number
print(square_num(3))            # 9

concatenate = lambda x : "-" + x  # Using lambda to concatenate
print(concatenate('hello'))       # -hello

divide_by_three = lambda x : x / 3  # Using lambda to divide any given number by 3
print(divide_by_three(9))           # 3.0
