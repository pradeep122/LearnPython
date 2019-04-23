#  Write a program to translate characters to emoji's
message = input("Message: ")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😔",
    ":P": "😜"
}
result = ""
for word in words:
    result += emojis.get(word, word) + " "
print(result)
