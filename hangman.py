import random

wordlist = ["dog", "window", "foliage", "computer", "python", "bench"]
def hangman():
    global wordlist
    random_index = random.randint(0, len(wordlist)-1)
    gamemode = input("Welcome to Hangman! Type 1 to choose your own word. Type 2 to choose a random word from the word list!")
    if gamemode == "1":
        word = input("Player One, type a word for Player Two to guess:")
        if word not in wordlist:
            wordlist.append(word)
        print(wordlist)
    elif gamemode == "2":
        word = wordlist[random_index]
    wrong = 0
    stages = ["",
"________ ", "| ", "|  |", "|  0", "|/|\ ", "|/ \ ", "|  " ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    while wrong < len(stages) - 1:
        msg = "Guess a letter:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong + 1]))
        print("You lose! The word was {}.".format(word))
    repeat = input("Type p to play again!")
    if repeat == "p" or repeat == "P":
        hangman()
    else:
        print("Thanks for playing!")
    


hangman()
