secret_message = input("Enter your message: ")
encrypted_message = ""

def to_binary(char):
    return ord(char)

def encrypt_binary(binary_num):
    if (binary_num == 32):
        return binary_num
    elif (binary_num >= 120 and binary_num <= 122):
        return binary_num - 23
    elif (binary_num >= 88 and binary_num <= 90):
        return binary_num - 23
    else:
        return binary_num + 3

def decrypt_binary(binary_num):
    return chr(binary_num)


for char in secret_message:
    encrypted_message += str(decrypt_binary(encrypt_binary(to_binary(char))))

print("secret message", secret_message)
print("encrypted message", encrypted_message)