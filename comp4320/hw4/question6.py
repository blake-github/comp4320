

# Question 6 
# Exhaustive key search for shift cipher
# Blake Moore

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inputString = "BEEAKFYDJXUQYHYJIQRYHTYJIQFBQDUYJIIKFUHCQD"
x = 0
while x < 26:
    x = x + 1
    inputString = inputString.upper()
    decrypted = ""
    for character in inputString:
        found = alphabet.find(character)
        newLocation = found - x
        if character in alphabet:
            decrypted = decrypted + alphabet[newLocation]
        else:
            decrypted = decrypted + character
    cipherShift = str(x)
    print("Cipher shift: " + cipherShift)
    print("Decrypted message:")
    print(decrypted + "\n")
    
    
    