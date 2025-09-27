import random as r
def c(*kelimeler):

    kelims = []
    for kelime in kelimeler:
        kelims.append(kelime)

    return r.choice(kelims)

print(c("Aku","mau","makan"))