#Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
def divide(first, second):

    #Вернется ошибка, при условии, что число равно нулю
    if second == 0:
        return 'Ошибка, деление на 0 Запрещено!'

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