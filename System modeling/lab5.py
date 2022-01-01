def association(rl1, rl2):
    rl1_list = rl1.split('.')
    rl2_list = rl2.split('.')
    
    return f'0.{int(rl1_list[1])+int(rl2_list[1])}.' + '.'.join(rl1_list[2:]) + '.' + '.'.join(rl2_list[2:])   


def comparison(rl1, rl2):
    rl1_len = int(rl1[2])
    if rl1[4] != '.':
        rl1 = rl1[4:].split('.')
    else: 
        rl1 = rl1[5:].split('.')

    rl2_len = int(rl2[2])
    if rl2[4] != '.':
        rl2 = rl2[4:].split('.')
    else: 
        rl2 = rl2[5:].split('.')

    rl1 = [int(i) for i in rl1]
    rl2 = [int(i) for i in rl2]

    rl1.sort(reverse=True)
    rl2.sort(reverse=True)

    def compare(x):
        if x == rl1_len and x != rl2_len:
            return 'RL2 > RL1'
        elif x != rl1_len and x == rl2_len:
            return 'RL1 > RL2'
        elif x == rl1_len and x == rl2_len:
            return 'RL1 = RL2'
        elif rl1[x] > rl2[x]:
            return 'RL1 > RL2'
        elif rl2[x] > rl1[x]:
            return 'RL2 > RL1'
        else:
            x+=1
            return compare(x)

    res = compare(0)
    return res


def sorting(rl1, rl2):
    r = association(rl1, rl2)
    if r[4] != '.':
        x = r[4:].split('.')
    else: 
        x = r[5:].split('.')
    
    x = [int(i) for i in x]

    x.sort(reverse=True)
    res = f'0.{len(x)}'
    for i in x:
        res += '.'+str(i)
    return res


def reduction(rl1, rl2):
    res_list = []
    r = association(rl1, rl2)
    if r[4] != '.':
        r = r[4:].split('.')
    else: 
        r = r[5:].split('.')
    
    r = [int(i) for i in r]
    r.sort()

    for i in r:
        if i not in res_list:
            res_list.append(i)
        elif i in res_list:
            res_list.remove(i)
            res_list.append(int(i)+1)
    
    res_list.sort(reverse=True)
    res = f'0.{len(res_list)}'
    for i in res_list:
        res += '.'+ str(i)

    return res


def main():
    rl1_length = int(input("\nВвудіть довжину першого РЛ кода: "))
    rl1 = ''
    print("Введіть елементи: ")
    for i in range(0, rl1_length):
        rl1 += '.' + input()

    rl1 = '0.'+f"{rl1_length}"+rl1
    print(f'Перше РЛ число: {rl1}')
    
    rl2_length = int(input("Ввудіть довжину другого РЛ кода: "))
    rl2 = ''
    print("Введіть елементи: ")
    for i in range(0, rl2_length):
        rl2 += '.' + input()

    rl2 = '0.'+f"{rl2_length}"+rl2
    print(f'Друге РЛ число: {rl2}')

    print(f"Об'єднання: {association(rl1, rl2)}")
    print(f"Порівняння: {comparison(rl1, rl2)}")
    print(f"Сортування: {sorting(rl1, rl2)}")
    print(f"Приведення подiбних: {reduction(rl1, rl2)}\n")

    
if __name__ == "__main__":
    main()

    