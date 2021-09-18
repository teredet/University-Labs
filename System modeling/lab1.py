def module(num1, num2):
    '''
    Реализация одного модуля первого уровня
    '''
    if num1 and num2: res1 = 1
    else: res1 = 0

    if num1 or num2: res2 = 1
    else: res2 = 0

    return res1, res2


def level1(x1, x2, x3, x4, x5, x6):
    '''
    Проходимся по каждому ряду первых модулей и получаем по одной переменной
    '''

    # находим x6
    x1, temp1 = module(x1, x2)
    x2, temp2 = module(temp1, x3)
    x3, temp3 = module(temp2, x4)
    x4, temp4 = module(temp3, x5)
    x5, x6 = module(temp4, x6)

    # находим x5
    x1, temp1 = module(x1, x2)
    x2, temp2 = module(temp1, x3)
    x3, temp3 = module(temp2, x4)
    x4, x5 = module(temp3, x5)

    # находим x4
    x1, temp1 = module(x1, x2)
    x2, temp2 = module(temp1, x3)
    x3, x4 = module(temp2, x4)

    # находим x3
    x1, temp1 = module(x1, x2)
    x2, x3 = module(temp1, x3)

    # находим x2 and x1
    x1, x2 = module(x1, x2)

    print("Result after first level:")
    print(x1, x2, x3, x4, x5, x6)
    
    return x1, x2, x3, x4, x5, x6

def module2(num1, num2):
    '''
    Реализация одного модуля второго уровня
    '''
    if num1 == 1 and num2 == 0: res = 1
    elif num1 == 0 and num2 == 1: res = 1
    else: res = 0

    return res

def level2(x1, x2, x3, x4, x5, x6):
    '''
    Проходимся по модулям второго уровня
    '''    
    x6 = module2(x6, x5)
    x5 = module2(x5, x4)
    x4 = module2(x4, x3)
    x3 = module2(x3, x2)
    x2 = module2(x2, x1)
    x1 = module2(x1, 0)

    print("Result after second level:")
    print(x1, x2, x3, x4, x5, x6)
    return x1, x2, x3, x4, x5, x6

def module3(num1, num2, num3):
    '''
    Реализация одного модуля третьего уровня
    '''
    if num1 or num2 or num3: res = 1
    else: res = 0

    return res

def level3(x1, x2, x3, x4, x5, x6):
    '''
    Проходимся по модулям третьего уровня
    '''    
    y1 = module3(x1, x2, x3)
    y2 = module3(x1, x5, x4)
    y3 = module3(x4, x2, x6)
    print("Result after third level:")
    print(y1, y2, y3)


if __name__ == "__main__":
    '''
    This program implements a triangular processor module.
    '''
    values = input("Enter values (separated by ' '): ").split(' ')  # присваиваем переменной списко значений, которые вводит пользователь
    x1, x2, x3, x4, x5, x6 = [int(i) for i in values]  # присваиваем переменным значения
    x1, x2, x3, x4, x5, x6 = level1(x1, x2, x3, x4, x5, x6)  # вызывает функцию level1 и присваиваем её значения переменным чтобы передать их в след.функцию
    x1, x2, x3, x4, x5, x6 = level2(x1, x2, x3, x4, x5, x6)  # вызывает функцию level2 и присваиваем её значения переменным чтобы передать их в след.функцию
    level3(x1, x2, x3, x4, x5, x6)  # вызывает функцию level3
