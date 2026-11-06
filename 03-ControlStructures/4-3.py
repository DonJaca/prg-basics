plain_text = 'The early bird catches the worm'
encrypted_text = ''
for char in plain_text:
    if 'a' <= char <= 'z':
        char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    encrypted_text += char
print(plain_text)
print(encrypted_text)
