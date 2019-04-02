def emoji_converter(message):
    output = " "
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    for word in words:
        output += emojis.get(word, word) + " "
    return output


actual_message = input(">")
print(emoji_converter(actual_message))
