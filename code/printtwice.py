def printtwice(word):
    res = ""
    for i in word:
        res += i
        res += i
    return res


word = input()
print(printtwice(word))