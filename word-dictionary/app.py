from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter word you want learn meaning: ")
    if(word == ''):
        break
    print("Searching...")
    print(dictionary.meaning(word))