# Модуль 3_1 пространство имен.
# ==========================================
def count_calls(calls):
    print(calls)
count_calls(0)

cort_str_ = (0)
def String_info(str_):  # Содание функции
    global count_calls(calls += 1)
    global cort_str_  # Объявление глоальной пер. внутри функции
    long_str_ = len(str_)
    hi_str_ = str_.upper()
    low_str_ = str_.lower()
    cort_str_ = (long_str_, hi_str_, low_str_)


String_info("Рубеж")
print(cort_str_)
String_info("Приход")
print(cort_str_)


def is_contains(string, list_to_searh):
    # count_calls()
    # calls += 1
    for i in list_to_searh:
        if string.upper() == i.upper():
            return True
    return False


result_1 = is_contains('Добр', ['добропорядочный', 'добр', 'добрый'])
print(result_1)
result_2 = is_contains('Добр', ['добропорядочный', 'Добро', 'добрый'])
print(result_2)
# print(calls)
