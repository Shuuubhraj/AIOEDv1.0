import os
from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def encrypt_text(cipher, plaintext, key):
    if cipher == "AES":
        if len(key) not in (16, 24, 32):
            print("Invalid AES key length.")
            return None
        cipher = AES.new(key, AES.MODE_ECB)
    elif cipher == "DES":
        if len(key) != 8:
            print("Invalid DES key length.")
            return None
        cipher = DES.new(key, DES.MODE_ECB)
    elif cipher == "3DES":
        if len(key) != 16 and len(key) != 24:
            print("Invalid 3DES key length.")
            return None
        cipher = DES3.new(key, DES3.MODE_ECB)
    else:
        print("Invalid cipher mode.")
        return None

    ciphertext = cipher.encrypt(pad(plaintext.encode(), cipher.block_size))
    return ciphertext

def decrypt_text(cipher, ciphertext, key):
    if cipher == "AES":
        if len(key) not in (16, 24, 32):
            print("Invalid AES key length.")
            return None
        cipher = AES.new(key, AES.MODE_ECB)
    elif cipher == "DES":
        if len(key) != 8:
            print("Invalid DES key length.")
            return None
        cipher = DES.new(key, DES.MODE_ECB)
    elif cipher == "3DES":
        if len(key) != 16 and len(key) != 24:
            print("Invalid 3DES key length.")
            return None
        cipher = DES3.new(key, DES3.MODE_ECB)
    else:
        print("Invalid cipher mode.")
        return None

    plaintext = unpad(cipher.decrypt(ciphertext), cipher.block_size).decode()
    return plaintext

def display_banner():
    banner = '''
 █████╗ ██╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║██╔═══██╗██╔════╝██╔══██╗
███████║██║██║   ██║█████╗  ██║  ██║
██╔══██║██║██║   ██║██╔══╝  ██║  ██║
██║  ██║██║╚██████╔╝███████╗██████╔╝
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝╚═════╝  v1.0

By : Rajput Shubhraj Singh
AIOED: ALL in One Encryption Decryption
'''
    print(banner)

while True:
    display_banner()

    print("Select a cipher mode:")
    print("1. AES")
    print("2. DES")
    print("3. 3DES")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        break
    elif choice in ("1", "2", "3"):
        if choice == "1":
            cipher_mode = "AES"
        elif choice == "2":
            cipher_mode = "DES"
        elif choice == "3":
            cipher_mode = "3DES"

        print(f"Selected cipher mode: {cipher_mode}")
        print()

        while True:
            print("What would you like to do?")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Clear")
            print("0. Go back")

            action = input("Enter your choice: ")
            print()

            if action == "0":
                break
            elif action == "1":
                plaintext = input("Enter the plaintext to encrypt: ")
                print()
                key_length = None
                if cipher_mode == "AES":
                    key_length = "16, 24, or 32 bytes"
                elif cipher_mode == "DES":
                    key_length = "8 bytes"
                elif cipher_mode == "3DES":
                    key_length = "16 or 24 bytes"
                print(f"Enter the key (key length: {key_length}):")
                key = input().encode()
                print()
                ciphertext = encrypt_text(cipher_mode, plaintext, key)
                if ciphertext is not None:
                    print(f"Encrypted ciphertext: {ciphertext.hex()}")
                    print()
            elif action == "2":
                ciphertext_hex = input("Enter the ciphertext (in hexadecimal) to decrypt: ")
                print()
                key_length = None
                if cipher_mode == "AES":
                    key_length = "16, 24, or 32 bytes"
                elif cipher_mode == "DES":
                    key_length = "8 bytes"
                elif cipher_mode == "3DES":
                    key_length = "16 or 24 bytes"
                print(f"Enter the key (key length: {key_length}):")
                key = input().encode()
                print()
                ciphertext = bytes.fromhex(ciphertext_hex)
                plaintext = decrypt_text(cipher_mode, ciphertext, key)
                if plaintext is not None:
                    print(f"Decrypted plaintext: {plaintext}")
                    print()
            elif action == "3":
                clear_screen()
            else:
                print("Invalid choice.")
                print()
    else:
        print("Invalid choice.")
        print()
