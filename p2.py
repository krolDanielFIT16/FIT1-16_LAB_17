import pandas as pd

words = []
out = open("output.txt", "w", encoding="utf-8")

with open("text.txt", encoding="utf-8") as f:
    for line in f.readlines():
        words.extend([x.replace('\n', '') for x in line.split(" ")])

words = pd.Series(words, dtype="string")
print(words)


def func(word: str):
    charset = "АЕЄИІЇОУЮЯ"
    charset += charset.lower()

    if len(list(filter(lambda x: x in charset, word))) > 3:
        out.write(word + "\n")


words.apply(func)
