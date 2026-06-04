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




print("==========MI-TASK 14N ============")

def palindrom_check(string):
    string = string.lower()
    
    reversed_string = string[::-1]
    
    return string ==reversed_string

print(palindrom_check("python"));
print(palindrom_check("lool"));
    
    
print("==========MI-TASK 15O ============")

def calculateSumOfNumber(arr):
    total = 0
    
    for item in arr:
        if type(item) == int:
            total = total + item
            
        elif type(item) == float:
            total = total + item
            
            
        else:
            pass
        
        
    return total

arr = [8, "99", '11', 1]

print(calculateSumOfNumber(arr))



print("==========MI-TASK 16P ============")

def objectToArray(obj):
    result = []
    
    for key in obj:
        result.append([key, obj[key]])
        
    return result 

print(objectToArray({"a": 8, "f": 99, "u": 23}));   