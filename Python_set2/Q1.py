#Write a function to extract words from the sentence that are repeated multiple times, the
#function must return value(s).
#Display those words with the ‘#’ separator (use the join function).
#For example: WORD1 # WORD2 # WORD3

def extract_repeated_words(sentence):
    words = sentence.lower().split()  # Convert sentence to lowercase
    word_counts = {}
    repeated_words = set()


    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        if word_counts[word] == 2:  # Add to set when it appears the second time
            repeated_words.add(word)


    return ' # '.join(repeated_words)

sentence = input("Enter a proper sentence with repeated words: ")
result = extract_repeated_words(sentence)
if result:
    print("Repeated words are:", result)
else:
    print("No repeated words found.")



# ------------------------------STEPS/PSUEDOCODE------------------------------

# START PROGRAM

# PROMPT THE USER TO ENTER A SENTENCE WITH REPEATED WORDS.
# PROCESS INPUT SENTENCE

# CONVERT THE SENTENCE TO LOWERCASE TO HANDLE CASE INSENSITIVITY.
# SPLIT THE SENTENCE INTO WORDS USING SPACES AS DELIMITERS.
# INITIALIZE DATA STRUCTURES

# CREATE AN EMPTY DICTIONARY WORD_COUNTS TO STORE THE COUNT OF EACH WORD.
# CREATE AN EMPTY SET REPEATED_WORDS TO STORE WORDS THAT APPEAR MORE THAN ONCE.
# LOOP THROUGH EACH WORD IN THE SENTENCE

# FOR EACH WORD IN THE LIST OF WORDS:
# INCREMENT THE COUNT OF THE WORD IN WORD_COUNTS (USING GET TO HANDLE NEW WORDS).
# IF THE WORD HAS BEEN ENCOUNTERED FOR THE SECOND TIME (COUNT EQUALS 2), ADD IT TO THE REPEATED_WORDS SET.
# FORMAT AND RETURN THE RESULT

# IF THERE ARE REPEATED WORDS, JOIN THEM WITH ' # ' TO CREATE A FORMATTED STRING AND RETURN IT.
# IF NO REPEATED WORDS ARE FOUND, RETURN AN EMPTY STRING.
# DISPLAY RESULT

# IF REPEATED_WORDS IS NOT EMPTY, PRINT THE REPEATED WORDS.
# IF NO REPEATED WORDS ARE FOUND, PRINT "NO REPEATED WORDS FOUND."
# END PROGRAM





