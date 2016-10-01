import random,string

def generator(n,s):
    i = 0
    textList = []
    text = ''
    while i<n:
        randomSpaceIndex = random.random()
        if randomSpaceIndex >= s:
            textList.insert(i,random.choice(string.ascii_letters))
            text = text + textList[i]
            i = i + 1
        else:
            text = text + ' '

    return text



n = input('Enter the length of the random text you want : ')
n = int(n)
s = input('Enter the frequency [0,1) of spaces you want : ')
s = float(s)

print(generator(n,s))

#textLength = n*(random.random())
#textLength = int(textLength)
#letter2 = random.choice(string.ascii_letters)
