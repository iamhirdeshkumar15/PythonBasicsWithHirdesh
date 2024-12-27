# Write a code to encode and decode a string.
# Sender
alphabets = 'abcdefghijklmnopqrstuvwxyz'
decode = input("Enter a Message")
encode = ''
for i in range (len(decode)):
    encode += alphabets[(alphabets.index(decode[i])+3)%26]
print(encode)



# Receiver
encode = input()
decode = ''
for i in range (len(encode)):
    decode += alphabets[(alphabets.index(encode[i])-3)%26]
print(decode)


