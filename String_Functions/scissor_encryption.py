secret_message = input("Enter your message: ")
num_shift = int(input("Enter number of characters to shift: "))
encrypted_message = ""
'''
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
'''
# Even Better Solution:
for char in secret_message:
    to_binary = ord(char)
    if (to_binary == 32):
        encrypted_message += str(chr(to_binary))
    elif (to_binary >= 120 and to_binary <= 122):
        # encrypted_message += str(chr(to_binary - 23))
        encrypted_message += str(chr(to_binary - (26 - num_shift)))
    elif (to_binary >= 88 and to_binary <= 90):
        # encrypted_message += str(chr(to_binary - 23))
        encrypted_message += str(chr(to_binary - (26 - num_shift)))
    else:
        # encrypted_message += str(chr(to_binary + 3))
        encrypted_message += str(chr(to_binary + num_shift))

print("secret message: ", secret_message)
print("encrypted message: ", encrypted_message)