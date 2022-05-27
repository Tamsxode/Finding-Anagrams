# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    # [assignment] Add your code here
    return sorted(str1) == sorted(str2)
     

str1 = "cat"
str2 = "act"

print(find_anagrams(str1, str2))
