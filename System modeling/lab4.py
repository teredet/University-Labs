def decimal_to_binary(n):
    '''Takes a 10-based number and returns a 2-based number.'''
    b = ''
    
    while n > 0:
        b = str(n % 2) + b
        n = n // 2   
    # or we can use bin(n)
    
    return b

def float_decimal_to_binary(n):
    '''Takes a 10-based number and returns a 2-based number.'''

    first = int(str(n).split('.')[0])
    second = float('0.'+str(n).split('.')[1])

    b = ''
    b2 = ''
    
    while first > 0:
        b = str(first % 2) + b
        first = first // 2   

    for i in range(1,11):
        temp = str(second * 2)[0]
        b2 = b2 + temp
        if second*2>1:
            second = second*2-1
        else:
            second = second*2
    
    res = f'{b}.{b2}'
    return res

def decimal_to_octal(n):
    '''Takes a 10-based number and returns a 8-based number.'''
    o = ''
    
    while n > 0:
        o = str(n % 8) + o
        n = n // 8
    # or we can use oct(n)
    
    return o

def decimal_to_hexadecimal(n):
    '''Takes a 10-based number and returns a 16-based number.'''
    h= ''
    
    d_h = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
    
    while n > 0:
        h = d_h[n % 16] + h
        n = n // 16
    # or we can use hex(n)

    return h

def decimal_to_RL(n):
    '''Takes a 10-based number and returns a RL code.'''
    if n - int(n) == 0:
        b = decimal_to_binary(int(n))[::-1]
        RL = ''
        c = 0
        for i in range(0, len(b)):
            if b[i] == '1': 
                RL = '.' + f'{i}' + RL
                c += 1

        RL = '.' + str(c) + RL

        if n > 0: RL = '0' + RL
        else: RL = '1' + RL

        return RL
    else:
        b = float_decimal_to_binary(n)

        first = b.split('.')[0][::-1]
        second = '0.'+b.split('.')[1]
        RL = ''
        c = 0

        for i in range(0, len(second)):
            if second[i] == '1': 
                RL = RL + '.' + f'-{i-1}'
                c += 1

        for i in range(0, len(first)):
            if first[i] == '1': 
                RL = '.' + f'{i}' + RL
                c += 1

        RL = '.' + str(c) + RL

        if n > 0: RL = '0' + RL
        else: RL = '1' + RL

        return RL


if __name__ == "__main__":
    print("")

    number = float(input("Enter the number in decimal: ")) # присваиваем переменной списко значений, которые вводит пользователь

    print("")

    if number - int(number) == 0:
        # если число целое
        number = int(number)    
    
        print("Binary: ",decimal_to_binary(number)) # вызов функции которая печатает результат в 2-чной системе исчесления
        print("Octal: ",decimal_to_octal(number)) # вызов функции которая печатает результат в 8-ричной системе исчесления
        print("Hexadecimal: ", decimal_to_hexadecimal(number)) # вызов функции которая печатает результат в 16-ричной системе исчесления
        print("RL code: ", decimal_to_RL(number)) # вызов функции которая печатает результат в виде РЛ кола
    else:    
        # если число дробное
        print("Binary: ",float_decimal_to_binary(number)) # вызов функции которая печатает результат в 2-чной системе исчесления
        print("Octal: ",decimal_to_octal(int(number))) # вызов функции которая печатает результат в 8-ричной системе исчесления
        print("Hexadecimal: ", decimal_to_hexadecimal(int(number))) # вызов функции которая печатает результат в 16-ричной системе исчесления
        print("RL code: ", decimal_to_RL(number)) # вызов функции которая печатает результат в виде РЛ кола

    print("")