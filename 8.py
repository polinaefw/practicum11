def sort_string(text):
    chars = list(text)
    chars.sort()
    sorted_text = ''.join(chars)
    return sorted_text

user_input = input()

print(sort_string(user_input))