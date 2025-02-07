from art import logo


print(logo)
huruf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text, shift):
    encrypted_text = ""
    for c in text:
        if c.isalpha():  
            index = huruf.index(c)  
            new_index = (index + shift) % 26  
            encrypted_text += huruf[new_index]  
        else:
            encrypted_text += c  
    print(f"Here's the encoded result: {encrypted_text}")
    return encrypted_text  

def decode(text, shift):
    decoded_text = ""
    for c in text:
        if c.isalpha():  
            index = huruf.index(c)  
            new_index = (index - shift) % 26  
            decoded_text += huruf[new_index]  
        else:
            decoded_text += c  
    print(f"Here's the decoded result: {decoded_text}")

# Loop utama program
while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Invalid input! Please enter 'encode' or 'decode'.")
        continue  # Kembali ke awal loop jika input tidak valid

    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))

    if direction == "encode":
        encrypted_message = encode(text, shift)
    elif direction == "decode":
        decode(text, shift)

    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if repeat != "yes":
        print("Goodbye!")
        break  # Keluar dari loop jika pengguna memilih "no"
