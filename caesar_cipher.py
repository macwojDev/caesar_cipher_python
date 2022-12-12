# ascii uppercase 65-90 lowercase 97-122
# function
def encript(word, key):
    message = ''
    for x in word:
    # check if x is a letter
        if x.isalpha():
            num = ord(x)
            num += key
            if x.isupper():
                if num > 90:
                    num-=26
            else:
                if num > 122:
                    num-=26
            message+=chr(num)
        else:
            message+=x
    return message
# instructions
word = input('Choose word: ')
key = int(input('And key? '))

print(encript(word,key))

