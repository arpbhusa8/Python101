def get_long_words(words):
    longWords= []
    for word in words:
        if len(word) > 3:
            longWords.append(word)
    return longWords

words = ['apple','banana','cherry','date','elderberry','fig','grape','honeydew','kiwi','lemon']
print(get_long_words(words))


