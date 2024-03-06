Letters="abcdefghijklmnopqrstuvwxyz"
original=input(str())
word=original
for i in range(len(original)):
    if word[i]==original[i]:
        if word[i] in word[:i]:
        	a=word[:i]
        	b=word[i:]
        	b=b.replace(word[i],Letters[-Letters.index(word[i])-1])
        	word=a+b
        else:
        	word=word.replace(word[i],Letters[-Letters.index(word[i])-1])
    else:
        word=word
print(word,end="")
