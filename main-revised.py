run = True
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

wordList = []
validWords = []
words = open('sowpods.txt', 'r')
for line in words:
    wordList.append(line.strip().lower())

print("Welcome to the Scrabble Cheater! Learn to use me, and you could win yourself a scrabble game"
      ", or maybe even an English major degree!")
while run:
    dock = str(input("Enter your dock letters: ")).lower()
    dockLetters = list(dock)

    for word in wordList:
        Candidate = True
        currentDock = list(dockLetters)
        for letter in word:
            if letter not in currentDock:
                Candidate = False
                break
            else:
                currentDock.remove(letter)
        if Candidate:
            total = 0
            for letter in word:
                total = total + scores[letter]
            validWords.append([total, word])

    validWords.sort(reverse=True)

    for entry in validWords:
        score = entry[0]
        word = entry[1]
        print(str(score), word)

    keepItUp = str(input("Do you want to continue? (Yes or No)")).lower()
    if keepItUp == "no":
        run = False
    elif not(keepItUp == "yes" or "no"):
        run = False
    else:
        run = True
