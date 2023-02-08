def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    word_count = {}
    for word in file_contents:
        # removing punctuations
        clean_word = word
        for character in punctuations:
            clean_word = clean_word.replace(character, "")

        # ignoring case
        lower_clean_word = clean_word.lower()

        # add to dictionary if is not any of the 'uninteresting words'
        if lower_clean_word not in uninteresting_words:
            # look if there is a key for the current word
            if lower_clean_word in word_count.keys():
                # if there is, update the value
                word_count[lower_clean_word] = word_count[lower_clean_word] + 1
            # If there is not
            else:
                # Create the key with the initial value
                word_count[lower_clean_word] = 1

    return word_count


def main():
    the_file = open("The Works of Edgar Allan Poe.txt", "r")
    data = the_file.read()
    file_contents = data.replace('\n', ' ').split(" ")
    # file_contents = ['This', 'is', 'our', 'log', 'file', 'that', 'we', 'will', 'parse', 'using', 'Python', 'code.']

    dictionary = calculate_frequencies(file_contents)
    print(dictionary)


main()
