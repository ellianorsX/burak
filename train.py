def gaplarniReverse(text):
    words = text.split(" ")
    
    reversed_words = [word[::-1] for word in words]
    
    return " ".join(reversed_words)


print(gaplarniReverse("I am Developer and Engineer"))

    