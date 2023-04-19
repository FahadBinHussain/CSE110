def remove_characters(sentence, position):
    keep = ""
    remove = ""

    for index, char in enumerate(sentence):
        
        if index % position == 0 and index != 0:
            remove += char
        else:
            keep += char

    new_sentence = keep + remove

    return new_sentence

sentence = "I love programming."
position = 3
new_sentence = remove_characters(sentence, position)
print(new_sentence)
