message = input(">")
words = message.split(' ')
# print(words)
emojis = {
    ":)": "😀",
    ":(": "😞"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
