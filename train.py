# def gaplarniReverse(text):
#     words = text.split(" ")
    
#     reversed_words = [word[::-1] for word in words]
    
#     return " ".join(reversed_words)


# print(gaplarniReverse("I am Developer and Engineer"))


# print("==========MI-TASK 13M ============")

# def getSquareNumbers(numbers):
#     result = []
    
#     for raqam in numbers:
#         object = {
#             "number": raqam,
#             "square": raqam * raqam 
#         }
        
#         result.append(object)
        
        
#     return result


# print(getSquareNumbers([1, 2, 3, 4, 5]));




# print("==========MI-TASK 14N ============")

# def palindrom_check(string):
#     string = string.lower()
    
#     reversed_string = string[::-1]
    
#     return string ==reversed_string

# print(palindrom_check("python"));
# print(palindrom_check("lool"));
    
    
# print("==========MI-TASK 15O ============")

# def calculateSumOfNumber(arr):
#     total = 0
    
#     for item in arr:
#         if type(item) == int:
#             total = total + item
            
#         elif type(item) == float:
#             total = total + item
            
            
#         else:
#             pass
        
        
#     return total

# arr = [8, "99", '11', 1]

# print(calculateSumOfNumber(arr))



# print("==========MI-TASK 16P ============")

# def objectToArray(obj):
#     result = []
    
#     for key in obj:
#         result.append([key, obj[key]])
        
#     return result 

# print(objectToArray({"a": 8, "f": 99, "u": 23}));   


# print("==========MI-TASK 17Q ============")

# def hasProperty(obj: dict, prop: str) -> bool:
#     if prop in obj:
#         return True
#     else:
#         return False
    
    
# print(hasProperty({"job": "AI AGENT"}, "job"))   
# print(hasProperty({"job": "AI AGENT"}, "hobby")) 
# print(hasProperty({"phone": "Iphone"}, "earphone"))


# print("==========MI-TASK 18R ============")

# def calculate(str):
#     str = str.replace(" ", " ")
#     for operator in [" + ", " - ", " * ", " / "]:
#         if operator in str:
#             data = str.split(operator)
#             a = int(data[0])
#             b = int(data[1])
            
#             if operator == " + ":
#                 return a + b
#             elif operator == " - ":
#                 return a - b 
#             elif operator == " * ":
#                 return a * b
#             elif operator == " / ":
#                 return a / b 
            
# print(calculate(str("2 * 5")))   

# print(calculate(str( "20 / 4" )))         
        
        
        
# print("==========MI-TASK 19S ============")

# def forgetNumber(arr):
#     num = len(arr)
    
    
#     for i in range( num + 1 ):
#         if i not in arr:
#             return i
        

# print(forgetNumber([1, 3, 0])) 
# print(forgetNumber([4, 0, 3]))       


# print("==========MI-TASK 20T ============")

# def birlashishToArray(arr1, arr2):
#     result = []
#     i = 0
#     m = 0
    
#     while i < len(arr1) and m < len(arr2):
#         if arr1[i] <= arr2[m]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[m])
#             m += 1
 
#     result.extend(arr1[i:])
#     result.extend(arr2[m:]) 
           
#     return result    

# print(birlashishToArray([1, 4, 5, 6], [7, 8, 9]))



# print("==========MI-TASK 21V ============")

# def countChars(str):
#     result = {}
    
#     for EveryVerb in str:
#         if EveryVerb in result:
#             result[EveryVerb] = result[EveryVerb] + 1
    
#         else:
#             result[EveryVerb] = 1
        
#     return result

# print(countChars("respect")),
# print(countChars("congratulation!"))


# print("==========MI-TASK 22W ============")

# def slays_array(nums, size):
#     result = []
    
#     for i in range(0, 2, 4):
#         slays = nums[ i : i + size]
        
#         result.append(slays)
        
#         return result
    
# print(slays_array([1,2,3,4,5,6,7,8,9], 3))

# print(slays_array([2,4,6,7,8], 1))
        
        
# print("==========MI-TASK 23X ============")        
# def count_occurrences(obj, key):
#     count = 0
    
#     for kalit, door in obj.items():
        
#         if kalit == key:
#             count += 1
            
#     if type(door) == dict:
#         count += count_occurrences(door, key)
        
        
#     return count

# obj = {"model": "A", "s": {"model": "M"}, "B": "Steak"  }

# print(count_occurrences(obj, "model"))
# print(count_occurrences(obj, "B"))

print("==========MI-TASK 24Y ============")

def findInterSection(menu1, menu2):
    result = []
    for data in menu1:
        if data in menu2:
            result.append(data)
    
    return result

print(findInterSection([22, 53, 57], [53, 30, 57]))        
            