#Write a function to extract words from the sentence that are repeated multiple times, the
#function must return value(s).
#Display those words with the ‘#’ separator (use the join function).
#For example: WORD1 # WORD2 # WORD3

def extract_repeated_words(sentence):
    
    words = sentence.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    repeated_words = [word for word in words if word_counts[word] > 1]
    return ' # '.join(repeated_words)
    
sentence = "Pratham shah Pratham shah"
result = extract_repeated_words(sentence)
print(result)

# ------------------------------STEPS/PSUEDOCODE------------------------------
# FUNCTION extract_repeated_words(sentence):
# 	STEP 1: SPLITS THE STRING INTO LIST OF STRING AND STORE THEM INTO WORDS
# 	STEP 2: INITIALIZING ONE EMPTY DICTIONARY CALLED WORD_COUNTS FOR COUNT OF REPEATED WORDS AS WORD WILL BE KEY AND THEIR COUNT WILL BE 
#		VALUE
#	STEP 3: FOR EACH WORD IN THE LIST OF WORDS
#		A. IT CHECKS IF THE WORD ALREDY EXIST IN THE DICTIONARY THEN IT WILL INCREMENT BY 1
#		B. IT CHECKS IF THE WORD NOT EXIST IN DICTIONARY THEN IT WILL ADD IT WITH BY 1
#	STEP 4: INITIALIZING THE ONE EMPTY LIST(repeated_words) TO STORE THE WORDS THAT ARE REPEATED
#		A.FOR EACH WORD IN THE DICTIONARY IF THE ANY WORD'S VALUE WILL BE GREATER THAN 1 THEN IT WILL BE ADDED TO THE  LIST(repeated_words)
#       STEP 5: JOIN ALL THE WORDS IN THE LIST(repeated_words) WITH #
#	STEP 6: RETURN result AS A STRING.
# END



