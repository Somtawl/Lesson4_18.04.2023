array1_size = int(input("Введите размер массива 1 "))
array2_size = int(input("Введите размер массива 2 "))
array1 = []
array2 = []
result = []

for i in range(array1_size):
    array1.append(int(input("Введите элемент Массива 1 ")))

for j in range(array2_size):
    array2.append(int(input("Введите элемент Массива 2 ")))

for c in array1:
    for b in array2:
        if c == b:
            if c not in result:
                result.append(c)

if len(result) == 0:
    print("Нет решения")
    quit()

temp_num = result[0]

print(len(result))
for g in range(len(result) - 1):
    if g == len(result) - 1:
        break
    else:
        if result[g] > result[g + 1]:
            temp_num = result[g]
            result[g] = result[g + 1]
            result[g + 1 ] = temp_num


print("числа", result)