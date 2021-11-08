print("")
operations = int(input("Enter the number of operations: ")) # присваиваем переменной количество операций
res = {} # создаем пустой словарь

for i in range(1, operations+1): # запрашиваем у пользователя каждой операции и определяем её ранг
    line = input(f"{i} operation:")
    start = line.find('40') + 2
    end = start + 2

    res[i]=line[start:end]

for i in list(res.items()): # выводим номер операции и её ранг
    print(f"{i[0]} operation: rang {int(i[1])+1}")
print("")