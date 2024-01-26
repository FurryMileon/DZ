def filter_strings(strings):
    # Фильтрация строк по длине
    return [s for s in strings if len(s) <= 3]

# Запрос ввода от пользователя
user_input = input("Введите строки, разделённые пробелом: ")

# Преобразование введённой строки в массив строк
input_strings = user_input.split()

# Фильтрация массива строк
filtered_strings = filter_strings(input_strings)

# Вывод результата
print("Отфильтрованный массив строк, где длина каждой строки меньше или равна 3 символам:")
print(filtered_strings)
