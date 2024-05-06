secret_message = input("Enter your message: ")
key_num = int(input("Enter number of characters to shift: "))
encrypted_message = ""
'''
def to_binary(char):
    return ord(char)

def encrypt_binary(binary_num):
    if (binary_num == 32):
        return binary_num
    elif (binary_num >= 120 and binary_num <= 122):
        return binary_num - (26 - key_num)
    elif (binary_num >= 88 and binary_num <= 90):
        return binary_num - (26 -key_num)
    else:
        return binary_num + key_num

def decrypt_binary(binary_num):
    return chr(binary_num)


for char in secret_message:
    encrypted_message += str(decrypt_binary(encrypt_binary(to_binary(char))))

'''
# Even Better Solution:
for char in secret_message:
    to_binary = ord(char)
    if (to_binary == 32):
        encrypted_message += str(chr(to_binary))
    elif (to_binary >= 120 and to_binary <= 122):
        encrypted_message += str(chr(to_binary - (26 - key_num)))
    elif (to_binary >= 88 and to_binary <= 90):
        encrypted_message += str(chr(to_binary - (26 - key_num)))
    else:
        encrypted_message += str(chr(to_binary + key_num))
# '''
print("secret message: ", secret_message)
print("encrypted message: ", encrypted_message)