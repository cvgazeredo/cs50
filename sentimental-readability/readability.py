from cs50 import get_string

# Asks the user to type in some text
text = get_string("Text: ")

# Count the number of letters, words, and sentences in the text
letters = 0
words = 1
sentences = 0

for i in text:
    if i.isalpha():
        letters += 1
    elif i == " ":
        words += 1
    elif i == "." or i == "!"or i == "?":
        sentences += 1

# Outputs the grade level for the text, according to the Coleman-Liau formula
index = 0.0588 * ( letters / words * 100) - 0.296 * ( sentences / words * 100) - 15.8

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade", round(index))