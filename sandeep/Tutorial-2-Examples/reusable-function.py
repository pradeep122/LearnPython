def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😔",
        ":P": "😜"
    }
    result = ""
    for word in words:
        result += emojis.get(word, word) + " "
    return result


message = input("Message: ")
# result = emoji_converter(message)
print(emoji_converter(message))
