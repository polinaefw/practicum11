def sort_string(text):
    '''преобразуем строку в список символов, сортируем список, превращаем обратно в строку'''
    chars = list(text)
    chars.sort()
    sorted_text = ''.join(chars)
    return sorted_text

user_input = input()

print(sort_string(user_input))
