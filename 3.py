text = input()

punctuation = ".,!?;:()\"'-—"

words = []
for word in text.split():
    for punct in punctuation:
        word = word.replace(punct, '')
    words.append(word)
print(words)