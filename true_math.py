
#Бесконечность импортировать из встроенной библиотеки math (from math import inf)
from math import inf

#Функция возвращать результат деления на 0 - бесконечность.
def divide(first, second):
    if second == 0:
        return inf

    #выводим результат при делении числа на число
    else:
        result = first / second
        return result


'''
#Тесты
result1 = divide(69, 3)

result2 = divide(3, 0)

result3 = divide(49, 7)

result4 = divide(15, 0)

print(result1)

print(result2)

print(result3)

print(result4)
'''