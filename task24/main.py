from random import randint

number_of_bushes = int(input("Введите количество кустов "))
garden = {}

for i in range (number_of_bushes):
    bush_number = i + 1
    harvest = randint(1,10)
    garden[bush_number] = harvest

max_harvest = 0
bush = 0
print(garden)
for i in range(1, number_of_bushes + 1):
    if i == 1:
        current_harvest = int(garden[number_of_bushes]) + int(garden[i]) + int(garden[i + 1])
    elif i == number_of_bushes:
        current_harvest = int(garden[i - 1]) + int(garden[i]) + int(garden[1])
    else:
        current_harvest = int(garden[i - 1]) + int(garden[i]) + int(garden[i + 1])
    if current_harvest > max_harvest: 
        max_harvest = current_harvest
        bush = i

print(bush)