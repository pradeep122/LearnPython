
message = input("> ")
words = message.split(' ')
print(words)

emoji_map = {
    ':)': '🌝',
    ':(': '😟',
    ':|': '😑'
}

# using string.replace method
# for emoji in emoji_map:
#     message = message.replace(emoji, emoji_map.get(emoji))

# print(message)


output = ''
for word in words:
    output += emoji_map.get(word, word) + ' '

print(output)


# Converting into a function

def convert_emojis(message):
    words = message.split(' ')

    emoji_map = {
        ':)': '🌝',
        ':(': '😟',
        ':|': '😑'
    }

    output = ''
    for word in words:
        output += emoji_map.get(word, word) + ' '

    return output


message = input('> ')
print(convert_emojis(message))
