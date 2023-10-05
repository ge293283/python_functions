"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import datetime


def delimiter(char="*", qua=10, end_char=''):
    """
    Функция для печати разделителя
    :param char: символ разделителя
    :param qua: длина строки (кол-во символов)
    :param end_char: последний символ (для переноса каретки)
    :return: None
    """
    print(char * qua, end_char)


def current_time_op():
    """
    Функция для получения даты и времени выоплнения операции
    Необходима библиотека datetime
    :return:
    """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def history_add(history_dict, operation_description):
    """
    Функция для добавления данных операции в историю
    :param history_dict: переменная для хранения истории (dict)
    :param operation_description: данные операции (list)
    :return: 2023-10-05 18:03:05
    """
    history_dict.update({current_time_op(): operation_description})


def balance_change(op, balance, input_num, history):
    """
    Функция для изменения баланска
    :param op: вид операции
    :param balance: переменная для хранения баланса (float)
    :param input_num: число на которое изменится баланс
    :param history: переменная для хранения история операций (dict)
    :return:
    """
    if op == "+":
        delimiter()
        # Операция + запись в историю
        balance += input_num
        history_add(history, ["пополнение счета", input_num, balance])
        # Вывод на экран
        print(f"\nCчёт успешно пополнен на {input_num} р.")
        print(f"Ваш баланс: {balance} р.")
        delimiter("*", 10, "\n")
        return balance
    elif op == "-":
        delimiter()
        # Проверка баланса на лачие срадств для совершения покупки
        if balance > input_num:
            # Операция + запись в историю
            balance -= float(input_num)
            history_add(history, ["покупка", input_num, balance])
            # Вывод на экран
            print(f"\nСовершена покупка на {input_num} р.")
            print(f"Ваш баланс: {balance} р.")
            delimiter("*", 10, "\n")
            return balance
        else:
            # Запись в историю
            history_add(history, ["отказ в операции", input_num, balance])
            # Вывод на экран
            print(f"\nНедостаточно средств!")
            print(f"Ваш баланс: {balance} р.")
            delimiter("*", 10, "\n")
            return balance


def history_print(histori_dict):
    """
    Функция для вывода на экран истории операций
    :param histori_dict:
    :return: None
    """
    delimiter()
    delimiter()

    for timestamp, operation in histori_dict.items():
        print(f"Дата и время: {timestamp}")
        print(f"Операция: {operation[0]}")
        print(f"Сумма: {operation[1]} р.")
        print(f"Баланс: {operation[2]} р.\n")

    delimiter()
    delimiter("*", 10, "\n")


# Общий баланс и история операций
user_balance = 0.0
user_history = {}

# Основное меню
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход \n')

    choice = input('Выберите пункт меню: ')
    # Пополнение баланса
    if choice == '1':
        replenishment = float(input("Введите сумму для пополнения счета: "))
        user_balance = balance_change("+", user_balance, replenishment, user_history)
    # Списание
    elif choice == '2':
        write_off = float(input("Введите сумму для списания: "))
        user_balance = balance_change("-", user_balance, write_off, user_history)
    # История операций
    elif choice == '3':
        history_print(user_history)
    # Выход
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
