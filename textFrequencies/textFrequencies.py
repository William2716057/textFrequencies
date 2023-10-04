from tkinter import WORD
import matplotlib.pyplot as plt

#function to create dictionary for word storage
def stored(text, wordstoCount):
    #dictionary
    wordCounts = {word: 0 for word in wordstoCount}

    #split text into words
    words = text.split()

    #count words
    for word in words:
        if word in wordstoCount:
            wordCounts[word] += 1

    return wordCounts

#function to plot words

def wordplots(wordCounts):
    #extract words and counts from wordCounts dictionary
    words = list(wordCounts.keys())
    counts = list(wordCounts.values())

    plt.figure(figsize=(10, 6))
    plt.plot(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Occurrences')
    plt.title('Word Occurrences')
    plt.xticks(rotation=45, fontsize=10)

    plt.show()

inputText = """this is some text text this this this this""" #add sample text here 
 

wordstoCount = ["this", "text", "this", "some", "is", "hat", "shoe"] #add words between quotes

Counts = stored(inputText, wordstoCount)

wordplots(Counts)