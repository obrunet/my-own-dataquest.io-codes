## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, row in enumerate(things):
    row.append(trees[i])

print(things)

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled=[2*apple_price for apple_price in apple_prices]
apple_prices_lowered=[apple_price-100 for apple_price in apple_prices]

## 5. Counting Female Names ##

name_counts={}
for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    if birth_year == '':
        birth_year = '0'
    birth_year = int(birth_year)
    if row[3] == 'F' and birth_year > 1940:
        name=row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

print(name_counts)
        

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for value in values:
    check = value is not None and value > 30
    checks.append(check)

## 8. Highest Female Name Count ##

max_value=None
for name in name_counts:
    count=name_counts[name]
    if max_value is None or count > max_value:
        max_value = count
        

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for key, value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for name, count in name_counts.items():
    if count == 2:
        top_female_names.append(name)
print(top_female_names)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts={}
count=0
for row in legislators:
    birth_year = row[2].split('-')[0]
    if birth_year =='':
        birth_year = 0
    birth_year = int(birth_year)
    if row[3] == 'M' and birth_year > 1940:
        if row[1] in male_name_counts:
            male_name_counts[row[1]] += 1
        else:
            male_name_counts[row[1]] = 1

highest_male_count = None
for name, count in male_name_counts.items():
    if highest_male_count is None or count > highest_male_count:
        highest_male_count = count

for name, count in male_name_counts.items():
    if count == highest_male_count:
        top_male_names.append(name)