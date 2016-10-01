import random,string

def generator(n):
    i = 0
    textList = []
    text = ''
    while i<n:
        textList.insert(i,random.choice(string.ascii_letters))
        text = text + textList[i]
        i = i + 1

    return text



n = input('Enter the length of the random text you want : ')
n = int(n)

print(generator(n))

#textLength = n*(random.random())
#textLength = int(textLength)
#letter2 = random.choice(string.ascii_letters)
