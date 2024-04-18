import os
import asyncio
from decrypt_methods.decrypt import decrypt1
from decrypt_methods.decrypt import analyze

async def iterate_keys(method, ciphertext, keys, output_file_path):
    
    with open(output_file_path, 'a') as output_file:
        output_file.write("\nSTART OF ITERATE KEYYYYYSSS\n")
        if method.__name__ != "analyze":
            for key in keys:
                decrypted_text = method(ciphertext, key)

                print("\n")
                output_file.write("\n\n")

                print(f"Key: {key}, Decrypted Text:\n {decrypted_text}")
                output_file.write(f"Key: {key}, Decrypted Text:\n {decrypted_text}")
        else:
            await analyze(ciphertext, output_file_path)

def load_ciphertext(file_path):
    with open(file_path, 'r') as file:
        ciphertext = file.read()
        return ciphertext


# Example ciphertext (replace with your ciphertext)
ciphertext_file = "message_1.txt"
ciphertext = load_ciphertext(ciphertext_file)

# Output
output_file_path = "output.txt"


# Example dictionary of keys to try
keys_to_try = ["KEY1", "KEY2", "KEY3","ACSM"]  # Replace with actual keys

# Iterate through decryption methods and test each one
decrypt_methods = [decrypt1, analyze]



async def main():
    with open(output_file_path, 'w') as output_file:

        for method in decrypt_methods:

            print(f"Testing decryption method: {method.__name__}")
            output_file.write(f"Testing decryption method: {method.__name__}")

            print("=" * 50)
            output_file.write("=" * 50 + "\n")


            await iterate_keys(method, ciphertext, keys_to_try, output_file_path)

            output_file.write("\n")
            print()

asyncio.run(main())