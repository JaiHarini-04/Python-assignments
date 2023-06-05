def most_frequent(string):
    # Count the frequency of each character in the string
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Sort the characters based on their frequency in decreasing order
    sorted_chars = sorted(char_freq, key=char_freq.get, reverse=True)
    
    # Print the characters in decreasing order of frequency
    for char in sorted_chars:
        print(char, char_freq[char])

# Example usage
string = "Really Amazing!"
most_frequent(string)