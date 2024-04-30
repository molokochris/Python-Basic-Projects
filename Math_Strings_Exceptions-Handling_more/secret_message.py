message = str(input("Please enter your message in uppercase: "))
secret_message = ""
decrypted_message = ""
for char in message:
    secret_message += str(ord(char))

for i in range(0, len(secret_message)-1, 2):
    decrypted_message += chr(int(secret_message[i] + secret_message[i + 1]))

print("secret message: ", secret_message)
print("decrypted message: ", decrypted_message)