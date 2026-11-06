text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

index = 0
while index < len(text):
    char = text[index]
    if char in vowels:
        vowel_count += 1
    index += 1

print(f"The number of vowels in the text is: {vowel_count}")
