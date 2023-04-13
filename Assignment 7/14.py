def remove_characters(sentence, position):
    keep = ""
    remove = ""

    # Iterate over the characters in the sentence
    for index, char in enumerate(sentence):
        # Check if the index is divisible by the given position and not equal to 0
        if index % position == 0 and index != 0:
            remove += char
        else:
            keep += char

    # Concatenate the keep and remove strings
    new_sentence = keep + remove

    return new_sentence

# Example usage
sentence = "I love programming."
position = 3
new_sentence = remove_characters(sentence, position)
print(new_sentence)
