calls = 0 #Создаем переменную calls = 0 вне функций
def count_calls():# Функция count_calls подсчитывающая вызовы остальных функций.
    global calls
    calls += 1
def string_info(string): #Функция string_info принимает аргумент - строку и возвращает
    # кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search): #Функция is_contains принимает два аргумента:
    # строку и список, и возвращает True, если строка находится в этом списке,
    # False - если отсутствует.
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
