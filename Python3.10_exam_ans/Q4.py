def get_article(word):
    """
    Function to determine the correct article ('A' or 'An') for a given noun.
    If the word starts with a vowel (a, e, i, o, u), it returns 'An'.
    Otherwise, it returns 'A'.
    """
    vowels = "aeiou"
    return "An" if word[0].lower() in vowels else "A"

def format_nouns_sentence(nouns):
    """
    Function to format a list of nouns into a grammatically correct sentence.
    - Adds the correct article ('A' or 'An') before each noun.
    - Joins words with commas, except for the last two, which are joined by 'and'.
    - Starts with a capital letter and ends with a period.
    """
    if len(nouns) < 2:
        return "Please enter at least two nouns."

    # Add articles to each noun
    nouns_with_articles = [f"{get_article(noun)} {noun}" for noun in nouns]

    # Create a sentence with proper punctuation
    if len(nouns_with_articles) == 2:
        sentence = f"{nouns_with_articles[0]} and {nouns_with_articles[1]}."
    else:
        sentence = f"{', '.join(nouns_with_articles[:-1])} and {nouns_with_articles[-1]}."

    # Capitalize first letter and return sentence
    return sentence.capitalize()

def main():
    """
    Main function to take user input for nouns and print a grammatically correct sentence.
    """
    num_nouns = int(input("Enter the number of nouns: "))
    
    if num_nouns < 2:
        print("Please enter at least two nouns.")
        return

    nouns = [input(f"Enter noun {i+1}: ").strip().lower() for i in range(num_nouns)]

    formatted_sentence = format_nouns_sentence(nouns)
    print("\nFormatted Sentence:")
    print(formatted_sentence)

if __name__ == "__main__":
    main()

