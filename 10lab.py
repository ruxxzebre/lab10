author = "Pavlo Chaikovskyi 125B"
import numpy as np

"""
ОСНОВНІ :
1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n.
2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа.
3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.

ДОДАТКОВІ :
1. Сформувати функцію для введення з клавіатури послідовності чисел і виведення
її на екран у зворотному порядку (завершаючий символ послідовності – крапка)
2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе).
3. Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.
"""

"""
DECIMAL TO HEXADECIMAL ALGORITHM TAKEN FROM HERE :
https://www.permadi.com/tutorial/numDecToHex/
"""

def factorial_iter(n):
    temp = n
    while n > 1:
        n -= 1
        temp *= n
    return temp

def factorial_recc(n):
    if n == 0:
        return 1
    else:
        return n*factorial_recc(n - 1)

def digitalroot_iter(n):
    while True:
        temp = 0
        for i in str(n):
            temp += int(i)
        if temp//10 == 0:
            break
        else:
            n = temp
    return temp

def digitalroot_recc(n):
    if n//10 == 0:
        return n
    else:
        n = n%10 + digitalroot_recc(n//10)
        return digitalroot_recc(n)

def maxIndex_iter(array):
    temp = array[0, 0]
    for i in array:
        for j in i:
            if j > temp:
                temp = j
    return temp

def maxIndex_recc(array, temp=None, x = 0):
    if temp == None: temp = array[0, 0]

    if len(array) == 1:
        return temp
    else:
        if temp < array[0, x]:
            temp = array[0, x]

        if x == (len(array[0]) - 1):
            array = np.delete(array, 0, 0)
            x = -1
        return maxIndex_recc(array, temp, x + 1)


def backwards_iter(num_array):
    c = 0
    backwarded = []
    for i in range(1, len(num_array)):
        backwarded.append(num_array[c - i])
    return backwarded

def backwards_recc(num_array, backwarded = []):
    if len(num_array) == 1:
        backwarded.append(num_array[-1])
        return backwarded
    else:
        backwarded.append(num_array[-1])
        return backwards_recc(num_array[0:-1])

def simplenum_iter(num):
    if num != 1:
        counter = 0
        for i in range(1, num + 1):
            if num%i == 0:
                counter += 1
        return counter
    else:
        return 1

def simplenum_recc(num, divider=1):
    if divider == num:
        return 1
    else:
        if num%divider == 0:
            return 1 + simplenum_recc (num, divider + 1)
        else:
            return simplenum_recc (num, divider + 1)

def rth(reminders):
    #reminder to hexadecimal
    """
    This function converts reminders array got from funcs like decToHexadec,
    and make it hexadecimal.
    :param reminders:
    :return: hexadecimal number (in string)
    """
    reminders = map(str, reminders[::-1])
    table = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
    result = ''
    for i in reminders:
        if i not in table.keys():
            result += i
        else:
            result += table[i]
    return result

def decToHexadec_iter(num):
    """
    Yep, that's simply divider by 16.
    This func makes 'reminders' array, that'll be converted to hexadec num.
    :param num:
    :return:
    """

    reminders = []
    while num != 0:
        reminders.append(num%16)
        num //= 16
    #return reminders
    return rth (reminders)

def decToHexadec_recc(num, reminders = []):
    """
        Yep, that's simply divider by 16 (but recursive).
        This func makes 'reminders' array, that'll be converted to hexadec num.
        :param num:
        :return:
     """
    if num < 16:
        reminders.append(num)
        #return reminders
        return rth(reminders)
    else:
        reminders.append(num%16)
        num //=16
        return decToHexadec_recc(num, reminders)

if __name__ == "__main__":
    while True:
        b00l = input("Recursively? y/n ")
        what = int(input("Okay\nSo..\nWhat will you choose :\nFactorial (0)\nDigital root (1)\n"
                     "Max index of matrix n*n (2)\nBackward array (3)\n"
                     "Simplicity of num (4)\n or Decimal to hexadecimal translator (5)\n : "))

        if b00l in ('y', 'n') and what in range(0, 5 + 1):
            break

    if what == 0:
        n = int(input('Enter num : '))
        if b00l == 'y' :
            print(factorial_recc(n))
        elif b00l == 'n' :
            print(factorial_iter(n))
    elif what == 1:
        n = int (input ('Enter num : '))
        if b00l == 'y':
            print (digitalroot_recc(n))
        elif b00l == 'n':
            print(digitalroot_iter(n))
    elif what == 2:
        while True:
            n = int(input('Enter n : '))
            if n in range(1, 5 + 1):
                break

        array = np.random.randint(0, 100, size=(n, n))
        print(array)
        if b00l == 'y' :
            print(maxIndex_recc(array))
        elif b00l == 'n':
            print (maxIndex_iter(array))
    elif what == 3:
        array = input('Enter few values, separated by coma : \n').split(', ')
        if b00l == 'y' :
            print(backwards_recc(array))
        elif b00l == 'n':
            print (backwards_iter(array))
    elif what == 4:
        n = int(input("Enter num : "))
        if b00l == 'y' :
            print(simplenum_recc(n))
        elif b00l == 'n':
            print (simplenum_iter(n))
    elif what == 5:
        n = int(input("Enter decimal : "))
        if b00l == 'y' :
            print(decToHexadec_recc(n))
        elif b00l == 'n':
            print (decToHexadec_iter(n))
