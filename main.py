import argparse

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

wordList = []
validWords = []

parser = argparse.ArgumentParser(description='Help you win scrabble and Words with friends, '
                                             'and maybe even get you that english major!')
parser.add_argument("letters", type=str, help='Letters in your dock')
args = parser.parse_args()
dock = str(args.letters).lower()
dockLetters = list(dock)

words = open('sowpods.txt', 'r')
for line in words:
    wordList.append(line.strip().lower())

for word in wordList:
    candidate = True
    for letter in word:
        if letter not in dockLetters:
            candidate = False
        else:
            dockLetters.remove(letter)
    if candidate:
        total = 0
        for letter in word:
            total = total + scores[letter]
        validWords.append([total, word])

validWords.sort()

for entry in validWords:
    score = entry[0]
    word = entry[1]
    print(str(score), word)