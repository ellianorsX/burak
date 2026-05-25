def gaplarniReverse(text):
    words = text.split(" ")
    
    reversed_words = [word[::-1] for word in words]
    
    return " ".join(reversed_words)


print(gaplarniReverse("I am Developer and Engineer"))


print("==========MI-TASK 13M ============")

def getSquareNumbers(numbers):
    result = []
    
    for raqam in numbers:
        object = {
            "number": raqam,
            "square": raqam * raqam 
        }
        
        result.append(object)
        
        
    return result


print(getSquareNumbers([1, 2, 3, 4, 5]));