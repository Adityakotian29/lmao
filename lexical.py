# Function to check if a word is a Python keyword
def is_keyword(word):
    # List of Python keywords
    keywords = [
        "False", "None", "True", "and", "as", "assert", "break", "class", "continue",
        "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
        "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    ]
    return word in keywords  # Return True if the word is in the list of keywords

# Function to check if a character is a symbol
def is_symbol(ch):
    # List of valid symbols in Python
    symbols = "=+-*/%(){}[]:.,<>!|&^~"
    return ch in symbols  # Return True if the character is in the list of symbols

# Function to remove comments from the code
def remove_comments(code):
    result = ""  # Initialize an empty string to store the code without comments
    for line in code.split('\n'):  # Iterate through each line of the code
        if '#' in line:  # Check if the line contains a comment
            line = line[:line.index('#')]  # Remove everything after the '#' symbol
        result += line + '\n'  # Add the cleaned line to the result
    return result  # Return the code without comments

# Main function to perform lexical analysis
def lexical_analyzer(filename):
    # Open the file and read its contents
    with open(filename, "r") as f:
        code = f.read()

    # Remove comments from the code
    code = remove_comments(code)

    # Print the code after removing comments
    print("Code after removing comments:\n")
    print(code)
    print("\n--- Lexical Elements ---")

    # Initialize lists to store different types of lexical elements
    keywords = []  # List to store keywords
    identifiers = []  # List to store identifiers
    numbers = []  # List to store numbers
    symbols = []  # List to store symbols
    directives = []  # List to store preprocessor-like directives (e.g., "import", "from")

    word = ""  # Temporary variable to store the current word being processed
    for i in range(len(code)):  # Iterate through each character in the code
        ch = code[i]

        # Check if the character is alphanumeric or an underscore (part of a word)
        if ch.isalnum() or ch == '_':
            word += ch  # Add the character to the current word
        else:
            # If a word has been formed, classify it
            if word:
                if is_keyword(word):  # Check if the word is a keyword
                    if word not in keywords:  # Avoid duplicates
                        keywords.append(word)
                    if word == "import" or word == "from":  # Check for directives
                        directives.append(word)
                elif word.isdigit():  # Check if the word is a number
                    if word not in numbers:  # Avoid duplicates
                        numbers.append(word)
                else:  # Otherwise, classify it as an identifier
                    if word not in identifiers:  # Avoid duplicates
                        identifiers.append(word)
                word = ""  # Reset the word variable

            # Check if the character is a symbol
            if is_symbol(ch):
                if ch not in symbols:  # Avoid duplicates
                    symbols.append(ch)

    # Check the last word after the loop ends
    if word:
        if is_keyword(word):  # Check if the word is a keyword
            if word not in keywords:
                keywords.append(word)
        elif word.isdigit():  # Check if the word is a number
            if word not in numbers:
                numbers.append(word)
        else:  # Otherwise, classify it as an identifier
            if word not in identifiers:
                identifiers.append(word)

    # Print the results of the lexical analysis
    print("Keywords:", keywords)
    print("Identifiers:", identifiers)
    print("Numbers:", numbers)
    print("Preprocessor-like Directives:", directives)
    print("Symbols:", symbols)

# Run the lexical analyzer on a sample Python file
lexical_analyzer("lexsample.py")  # Replace "lexsample.py" with the name of your Python file
