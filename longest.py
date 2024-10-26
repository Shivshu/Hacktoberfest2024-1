def find_longest_word(file_path):
    try:
        longest_word = ""
        longest_length = 0

        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file contents
            text = file.read()

            # Split the text into words
            words = text.split()

            # Iterate through each word to find the longest one
            for word in words:
                # Remove punctuation and convert to lowercase
                cleaned_word = word.strip('.,!?";()').lower()
                if len(cleaned_word) > longest_length:
                    longest_word = cleaned_word
                    longest_length = len(cleaned_word)

        # Print the longest word and its length
        if longest_word:
            print(f"The longest word is '{longest_word}' with a length of {longest_length} characters.")
        else:
            print("No words found in the file.")

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")

# Specify the path to your text file
file_path = input("Enter the path to the text file: ")
find_longest_word(file_path)
