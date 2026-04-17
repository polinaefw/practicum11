HOLES_LETTERS = set('abdegopq')

def count_holes_in_word(word):
    """Подсчитывает количество букв с отверстиями в слове"""
    count = 0
    for letter in word:
        if letter in HOLES_LETTERS:
            count += 1
    return count

def count_letters_without_holes(word):
    """Подсчитывает количество букв без отверстий в слове"""
    count = 0
    for letter in word:
        if letter not in HOLES_LETTERS:
            count += 1
    return count

def count_holes_in_text(text):
    """Подсчитывает общее количество букв с отверстиями в тексте"""
    total = 0
    words = text.split()
    for word in words:
        total += count_holes_in_word(word)
    return total

def count_without_holes_in_text(text):
    """Подсчитывает общее количество букв без отверстий в тексте"""
    total = 0
    words = text.split()
    for word in words:
        total += count_letters_without_holes(word)
    return total

def get_words_with_two_or_more_holes(text):
    """Возвращает список слов, имеющих две и более буквы с отверстиями"""
    result = []
    words = text.split()
    for word in words:
        if count_holes_in_word(word) >= 2:
            result.append(word)
    return result

text = input()

holes_count = count_holes_in_text(text)
without_holes_count = count_without_holes_in_text(text)

words_with_two_holes = get_words_with_two_or_more_holes(text)

print(holes_count)
print(without_holes_count)
print(words_with_two_holes)