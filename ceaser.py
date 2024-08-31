def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            if mode == 'encrypt':
                shifted = (ord(char) - ascii_offset + shift) % 26
            else:  # decrypt
                shifted = (ord(char) - ascii_offset - shift) % 26
            result += chr(shifted + ascii_offset)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ").lower()
        
        if mode == 'q':
            print("Program Off")
            break
        
        if mode not in ['e', 'd']:
            print("Invalid mode. Please try again.")
            continue
        
        text = input("Enter the message: ")
        
        while True:
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift value must be between 1 and 25. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 25.")
        
        if mode == 'e':
            result = caesar_cipher(text, shift, 'encrypt')
            print(f"Encrypted message: {result}")
        else:
            result = caesar_cipher(text, shift, 'decrypt')
            print(f"Decrypted message: {result}")
        
        print()  # Add a blank line for readability

if __name__ == "__main__":
    main()