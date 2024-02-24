'''# Запросить у пользователя ввод двух чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Попытаться выполнить арифметические действия
try:
    # Сложение
    sum = num1 + num2
    print("Сумма чисел:", sum)

    # Вычитание
    difference = num1 - num2
    print("Разность чисел:", difference)

    # Умножение
    product = num1 * num2
    print("Произведение чисел:", product)

    # Деление
    quotient = num1 / num2
    print("Частное от деления чисел:", quotient)

except ZeroDivisionError:
    # Обработка ошибки деления на ноль
    print("Деление на ноль невозможно!")''' 

username = input("Введите имя пользователя: ")

try:
    if not username:
        raise ValidationError("Имя пользователя не может быть пустым.")
    elif not username_regex.match(username):
        raise ValidationError("Имя пользователя должно содержать только буквы, цифры и знак подчеркивания (_).")
except ValidationError as e:
    # Обработка пользовательского исключения
    print("Ошибка:", e.message)
else:
    # Имя пользователя допустимо
    print("Имя пользователя допустимо.")
