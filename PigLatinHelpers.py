def findFirstVowel(word):#returns the index of the first vowel
    for index in range(len(word)):
        if word[index] in 'aeiou':
            return index

    return 0 #means there is no vowel
def translateToPigLatin(word):#returns the translated word
    indexOfFirst = findFirstVowel(word)
    for index in range(indexOfFirst):
        word += word[index]
    word += 'ay'
    word = word[indexOfFirst:]
    return word
def exit(): # keeps screen open for user
    print("Press any key to exit")
    input()
    return none
