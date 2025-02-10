from art import logo

print(logo)

key = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def encryption(text, shift):
    """Fungsi untuk mengenkripsi teks dengan metode Caesar Cipher."""
    cipher_text = ""
    
    for c in text:
        if c.isalpha():  # Cek apakah karakter adalah huruf
            is_upper = c.isupper()  # Apakah karakter huruf besar
            c = c.upper()  # Konversi ke huruf besar
            
            new_index = (key.index(c) + shift) % 26  # Geser huruf
            new_char = key[new_index]  # Ambil huruf hasil pergeseran
            cipher_text += new_char if is_upper else new_char.lower()
        else:
            cipher_text += c  # Karakter non-huruf tidak dienkripsi
    
    return cipher_text

def decrypt(cipher_text, shift):
    "Fungsi untuk melakukan deskripsi cipher text"
    decrypt_text = ""
    
    for c in cipher_text:
        if c.isalpha():  # Cek apakah karakter adalah huruf
            is_upper = c.isupper()  # Apakah karakter huruf besar
            c = c.upper()  # Konversi ke huruf besar
            
            new_index = (key.index(c) - shift) % 26  # Geser huruf
            new_char = key[new_index]  # Ambil huruf hasil pergeseran
            decrypt_text += new_char if is_upper else new_char.lower()
        else:
            decrypt_text += c  # Karakter non-huruf tidak dienkripsi
            
    return decrypt_text

while True:
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()

    if user_input == 'encode':
        plain_text = input("Type your message:\n").strip()
        shift_number = int(input("Type the shift number:\n"))
        encrypted_text = encryption(plain_text, shift_number)  # Call encryption function
        print(f"Here's the encoded result: {encrypted_text}")
    elif user_input == 'decode':
        cipher_text = input("Type your message:\n").strip()
        shift_number = int(input("Type the shift number:\n"))
        decrypted_text = decrypt(cipher_text, shift_number)  # Call decryption function
        print(f"Here's the decoded result: {decrypted_text}")
    else:
        print("Invalid input, please try again!")
        continue  # Restart loop

    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").strip().lower()
    if again != 'yes':
        print("Goodbye!")
        break  # Exit loop

