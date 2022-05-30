from random import randint
import os
from art import *
from datetime import datetime

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
os.system("title " + "PyWordle by kChris")

line1 = ""
line2 = ""
line3 = ""

def correct(letter):
    global line1,line2,line3
    line1 += "|+++"
    line2 += f"|+{letter.upper()}+"
    line3 += "|+++"

def incorrect(letter):
    global line1,line2,line3
    line1 += "|---"
    line2 += f"|-{letter.upper()}-"
    line3 += "|---"

def wrong_position(letter):
    global line1,line2,line3
    line1 += "|///"
    line2 += f"|/{letter.upper()}/"
    line3 += "|///"

def congrats():
    print("")


def savescore(round):
    with open('stats.txt', 'a') as fd:
        fd.write(f"[{status}] - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - {selected_word} - {round}/6\n")

play = True
while play:
    round = 1
    clear()
    tprint("PyWordle")
    play = False
    import_words = open("words.txt", "r")
    word_list = []
    for x in import_words:
        word_list.append(x.replace("\n", ""))
    word_list_count = len(word_list)
    random_number = randint(0,len(word_list))
    selected_word = word_list[random_number]
    # CHEAT MODE
    print(selected_word)
    for num1 in range(1,7):
        guess = input(f"{num1}/6: ")
        while len(guess) != 5 or guess.isalpha() == False or guess.upper() not in word_list:
            if len(guess) != 5:
                print("!! PLEASE ENTER A 5 LETTER WORD (A-Z ONLY) !!")
            elif guess.isalpha() == False:
                print("!! PLEASE ENTER A 5 LETTER WORD (A-Z ONLY) !!")
            else:
                print(f"!! {guess} DOES NOT EXIST IN WORD LIST !!")
            guess = input(f"{num1}/6: ")
        guess = guess.upper()
        if round == 1 and (guess == selected_word):
            for num2 in range(5):
                correct(guess[num2])
            print(f"\n{line1}|\n{line2}|\n{line3}|\n")
            line1,line2,line3 = "","",""
            print(f"Congrats you got it in {round} try\n")
            status = "PASS"
            savescore(round)
            user_input = input("Would you like to play again? [y/n] ")
            while user_input.lower() not in ["y","n"]:
                print("!! PLEASE ENTER Y/N !!")
                user_input = input("Would you like to play again? [y/n] ")
            if user_input == "y":
                play = True
                break
            else:
                exit()
        if guess == selected_word:
            for num2 in range(5):
                correct(guess[num2])
            print(f"\n{line1}|\n{line2}|\n{line3}|\n")
            line1,line2,line3 = "","",""
            print(f"Congrats you got it in {round} tries\n")
            status = "PASS"
            savescore(round)
            user_input = input("Would you like to play again? [y/n] ")
            while user_input.lower() not in ["y","n"]:
                print("!! PLEASE ENTER Y/N !!")
                user_input = input("Would you like to play again? [y/n] ")
            if user_input == "y":
                play = True
                break
            else:
                exit()
        elif round == 6:
            for num2 in range(5):
                correct(guess[num2])
            print(f"\n{line1}|\n{line2}|\n{line3}|\n")
            line1,line2,line3 = "","",""
            print(f"You did not get todays wordle. The word was {selected_word}\n")
            status = "FAIL"
            savescore(round)
            user_input = input("Would you like to play again? [y/n] ")
            while user_input.lower() not in ["y","n"]:
                print("!! PLEASE ENTER Y/N !!")
                user_input = input("Would you like to play again? [y/n] ")
            if user_input == "y":
                play = True
                break
            else:
                exit()
        else:
            for num3 in range(5):
                if guess[num3] == selected_word[num3]:
                    correct(guess[num3])
                elif guess[num3] in selected_word and guess.count(guess[num3]) == selected_word.count(guess[num3]):
                    wrong_position(guess[num3])
                else:
                    incorrect(guess[num3])
            print(f"\n{line1}|\n{line2}|\n{line3}|\n")
            line1,line2,line3 = "","",""
            round += 1