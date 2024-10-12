class transformation_of_str:
    def __init__(self):
        pass
    
    # - Instance method in str mode
    def vowels_to_upper(self, char: str) -> str:
        vowels = "aeiouAEIOU"
        return ''.join([char.upper() if char in vowels else char for char in char])

# Output section
obj1 = transformation_of_str()
print(obj1.vowels_to_upper("=="))

obj2 = transformation_of_str()
print(obj2.vowels_to_upper("Hello, world!"))

obj3 = transformation_of_str()
print(obj3.vowels_to_upper("hello hi bye"))

# - Note: I used snake case rather than camel case, we got used to it po since 1st yr. 