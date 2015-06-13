import matplotlib.pyplot as plt
import nltk
from collections import defaultdict
#Jesse Bacon
#Putz Moby Dick into a Matrix and then graphs the charecter frequency distribution.
#Ready for Styles and everything.
#Requires NLTK and Matplotlib

words = nltk.corpus.gutenberg.words('melville-moby_dick.txt')

def letter_matrix():
    cake = {}
    alphabits = 'abcdefghijklmnopqrstuvwxyz'
    cake = defaultdict(int)
    for piece in alphabits:
        cake[piece] += 0
    return cake

def zip_book(wordlist,matrix):
    for word in wordlist:
        for letter in word:
            matrix[letter] += 1
    return cake

def make_frequency_chart(zipped_book, title):
    lines = []
    counts = []
    for line, count in zipped_book.items():
        lines.append(line)
        counts.append(count)
    plots = zip(lines,counts)
    plt.xlabel('Character')
    plt.ylabel('Count')
    #plt.legend #ary
    plt.plot(counts)
    plt.xticks(range(0,len(lines)), lines, rotation=0)
    plt.title(title)

matrix = letter_matrix()
frequency = zip_book(words, matrix)
make_frequency_chart(frequency, 'Moby Dick')