from collections import OrderedDict

punctuation = ".,!?;:()\"'-—«»"

def clean_word(word):
    '''убирает из слов знаки препинания'''
    for punct in punctuation:
        word = word.replace(punct, '')
    return word.lower()

lines = []
while True:
    line = input()
    if line == '':
        break
    lines.append(line)

text = ' '.join(lines)

words = []
for word in text.split():
    cleaned = clean_word(word)
    words.append(cleaned)

word_order = OrderedDict()
for word in words:
    if word in word_order:
        word_order[word] += 1
    else:
        word_order[word] = 1

sorted_words = sorted(word_order.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(word)
