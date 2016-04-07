"""
Check to see if it's a palindrome
If it isn't it will convert to palindrome
palindrome.py
Name: Jason Brooks
Email: jaythaceo@gmail.com
Twitter: @jaythaceo
"""
def is_palindrome(string_value):
    char_array = list(string_value)
    size = len(char_array)
    half_size = int(size / 2)
    for i in range(0, half_size):
        if char_array[i] != char_array[size - i - 1]:
            return False
    return True
def convert_to_palindrome(v):
    def action(string_value, chars):
        chars_to_append = list(string_value) [0:chars]
        chars_to_append.reverse()
        new_value = string_value + "".join(chars_to_append)
        if not is_palindrome(new_value):
            new_value = action(string_value, chars + 1)
        return new_value
    return action(v, 0)

user_input = raw_input("string to terminate program (exit to terminate program): ")
while user_input != "exit":
    print(str(convert_to_palindrome(user_input)))
    user_input = raw_input("string to check (exit to terminate): ")
    
    

    
