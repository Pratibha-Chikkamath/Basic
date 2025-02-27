import re

# Function to check if text starts with "palle"
def starts_with_palle(text):
    return bool(re.match(r"^palle", text))

# Function to check if text ends with "python"
def ends_with_python(text):
    return bool(re.search(r"python$", text))

# Function to check if text starts with "palle" and ends with "python"
def starts_with_palle_ends_with_python(text):
    return bool(re.match(r"^palle.*python$", text))

# Function to count digits in a text
def count_digits(text):
    return len(re.findall(r"\d", text))

# Function to count lowercase and uppercase letters
def count_letters(text):
    lowercase = len(re.findall(r"[a-z]", text))
    uppercase = len(re.findall(r"[A-Z]", text))
    return lowercase, uppercase

# Function to find words starting with "he", ending with "o", with at least 1 letter in between
def find_he_o_words(text):
    return re.findall(r"\bhe\w+o\b", text)

# Function to search for words that start with "he", contain any characters, and end with "o"
def find_he_any_o_words(text):
    return re.findall(r"\bhe.*?o\b", text)

# Example usage:
text = "palle is learning python. helo hero hellloooo he123o"
print("Starts with 'palle':", starts_with_palle(text))
print("Ends with 'python':", ends_with_python(text))
print("Starts with 'palle' and ends with 'python':", starts_with_palle_ends_with_python(text))
print("Number of digits:", count_digits(text))
lower, upper = count_letters(text)
print("Lowercase letters:", lower, "Uppercase letters:", upper)
print("Words starting with 'he' and ending with 'o':", find_he_o_words(text))
print("Words starting with 'he', any chars, and ending with 'o':", find_he_any_o_words(text))
