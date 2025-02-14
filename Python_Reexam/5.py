from collections import Counter
def word_frequency(string):
    '''
    Function to count frequency of each word and find most frequent word
    '''
    # Convert to lowercase and split into words
    words = string.lower().split()
    # Count the frequency of each word using Counter
    word_count = Counter(words)
    # Find the most frequent word
    most_frequent_word = word_count.most_common(1)[0]
    return word_count, most_frequent_word
#UserInput
string = input("Enter string:")
frequency, most_frequent = word_frequency(string)
print("Word Frequencies:", frequency)
print("Most Frequent Word:", most_frequent[0], "with frequency", most_frequent[1])
