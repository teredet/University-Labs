import lab5


def RL_sum(rl1, rl2):
    if rl1 == '0' or rl2 == '0':
        return 'Один із операндів дорівнює нулю'
    reducted_LR = lab5.reduction(rl1, rl2)

    return rl1[0] + reducted_LR[1:]


def RL_difference(rl1, rl2):
    if rl1 == '0' and rl2 == '0':
        return 0
    elif rl1 == '0' and rl2 != '0':
        return rl2
    elif rl1 != '0' and rl2 == '0':
        return rl1
    
    compered_LR = lab5.comparison(rl1, rl2)
    if compered_LR == 'RL1 > RL2':
        bigger_LR = rl1
        smaller_LR = rl2
    elif compered_LR == 'RL2 > RL1':
        bigger_LR = rl2
        smaller_LR = rl1
    elif compered_LR == 'RL1 = RL2':
        bigger_LR = rl1
        smaller_LR = rl2

    bigger_LR_list = bigger_LR.split('.')[2:]
    bigger_LR_list = [int(i) for i in bigger_LR_list]
    bigger_LR_list.sort()
    smaller_LR_list = smaller_LR.split('.')[2:]
    smaller_LR_list = [int(i) for i in smaller_LR_list]
    smaller_LR_list.sort()

    def del_i():
        del_list = []
        for i in smaller_LR_list:
            if i in bigger_LR_list:
                del_list.append(i)

        for i in del_list:
            smaller_LR_list.remove(i)
            bigger_LR_list.remove(i)

    def deconst_i():
        for i in bigger_LR_list:
            if i > smaller_LR_list[0]:
                y = bigger_LR_list.index(i)
                break
        x = bigger_LR_list.pop(y) -1
        
        while True:
            bigger_LR_list.append(x)
            if x == smaller_LR_list[0]:
                bigger_LR_list.append(x)
                break
            x -= 1


    while True:
        del_i()
        if smaller_LR_list == []:
            bigger_LR_list.sort(reverse=True)
            res = f'0.{len(bigger_LR_list)}'
            for i in bigger_LR_list:
                res += f".{i}"
            return res

        
        deconst_i()
        if smaller_LR_list == []:
            bigger_LR_list.sort(reverse=True)
            res = f'0.{len(bigger_LR_list)}.'
            for i in bigger_LR_list:
                res += f".{i}"
            return res



def main():
    rl1_length = int(input("\nВведіть довжину першого РЛ кода: "))
    rl1 = ''
    sign_rl1 = input('Введіть знак першого РЛ коду(0 - "+" або 1 -  "-"): ')
    print("Введіть елементи: ")
    for i in range(0, rl1_length):
        rl1 += '.' + input()

    rl1 = f'{sign_rl1}.{rl1_length}{rl1}'
    print(f'Перше РЛ число: {rl1}')
    
    rl2_length = int(input("Ввудіть довжину другого РЛ кода: "))
    rl2 = ''
    sign_rl2 = input('Введіть знак другого РЛ коду(0 - "+" або 1 -  "-"): ')
    print("Введіть елементи: ")
    for i in range(0, rl2_length):
        rl2 += '.' + input()

    rl2 = f'{sign_rl2}.{rl2_length}{rl2}'
    print(f'Друге РЛ число: {rl2}')

    print(f"Сума: {RL_sum(rl1, rl2)}")
    print(f"Різниця: {RL_difference(rl1, rl2)}\n")


if __name__ == "__main__":
    #main()

    print(RL_sum('0.7.11.9.4.0.-2.-7.-9', '0'))
    print(RL_difference('0.7.11.9.4.0.-2.-7.-9', '0'))

    #  '0.7.11.9.4.0.-2.-7.-9' '0.5.8.6.4.-1.-2'
    #  '0.10.45.38.23.22.18.11.8.7.4.0' '0.12.45.37.34.33.22.20.19.16.14.12.11.10'