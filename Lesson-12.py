import text_operations as t_o

text=input('Введите текст:')
oper=input('Для выбора операции введите ее номер: \n 1. Подсчитать количество символов в строке; \n 2. Подсчитать количество слов в строке; \n 3. Изменить регистр строки.\n')
if oper=='1':
    res=t_o.st_len(text)
    print(f'В строке {res} символов')
elif oper=='2':
    res=t_o.word_count(text)
    print(f'В строке {res} слов')
else:
    res=t_o.change_up_down(text)
    print('Регистр изменен \n',res)