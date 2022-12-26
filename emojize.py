import emoji

def main():
    emote = input('Input: ')
    print('Output: ', end='')
    print(emoji.emojize(emote))

main()