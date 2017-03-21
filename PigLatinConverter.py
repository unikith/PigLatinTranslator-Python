#Programmer: James Nelson
#Descriptin: this program takes an input English word and translates
#it to Pig Latin
#3/21: Added single word translation and interface loop
#TODO: add invalid input protection, sentence handling
import sys
import PigLatinHelpers

word = ''
while(word != 'EXIT'):
    print("Input a word to translate into pig latin or input EXIT to exit: ")
    word = input()
    if word != 'EXIT':
        word = PigLatinHelpers.translateToPigLatin(word)
        print(word)
exit()
