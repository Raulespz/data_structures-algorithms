def anagrams(word):
    if len(word) == 1:
        return [word]
    
    result = [] # empty list
    firstLetter = word[0]
    shorterAnagrams = anagrams(word[1:])
    for shorterAnagram in shorterAnagrams:
        for position in range(len(shorterAnagram) + 1): # 0, 1, 2, ..., len(shorterAnagram)
            newWord = shorterAnagram[:position] + firstLetter + shorterAnagram[position:] # insertion of first letter
            if newWord not in result:
                result.append(newWord)
    return result

if __name__ == "__main__":
    word = input("Give me a word: ")
    print(anagrams(word))