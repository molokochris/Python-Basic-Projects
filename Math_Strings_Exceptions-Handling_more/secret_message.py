message = str(input("Please enter your message in uppercase: "))
secret_message = ""
decrypted_message = ""
for char in message:
    if not(ord(char) == 32):
        secret_message += str(ord(char) - 32)
    else:
        secret_message += str(ord(char))

for i in range(0, len(secret_message)-1, 2):
    if not(int(secret_message[i] + secret_message[i + 1]) == 32):
        decrypted_message += chr(int(secret_message[i] + secret_message[i + 1]) + 32)
    else:
        decrypted_message += chr(int(secret_message[i] + secret_message[i + 1]))


print("secret message: ", secret_message)
print("decrypted message: ", decrypted_message)