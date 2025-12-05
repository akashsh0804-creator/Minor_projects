import random, string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

#creating keys
random.shuffle(key)

#__________Encrytion__________
def encryption():
    plain_text = input("Enter your text:")
    cypher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cypher_text += key[index]

    print(f"Your Normal text was    : {plain_text}")
    print(f"Your Encrypted text is  : {cypher_text}")

#__________Decrytion__________
def decryption():
    cypher_text = input("Enter your text:")
    plain_text = ""

    for letter in cypher_text:
        index = key.index(letter)
        plain_text += chars[index]

    print(f"Your Encrypted text was : {cypher_text}")
    print(f"Your Decrypted text is  : {plain_text}")

#__________Main function__________
def main():
    is_using = True

    print("***** This is a simple encryption tool *****")
    while is_using:
        print("What do you wish to do?", "1. Encryption of a text", "2. Decryption of the text", "3. Quit the program", sep="\n")
        user_input = int(input("Enter an option(1,2 or 3):"))

        if user_input == 1:
            encryption()
        elif user_input == 2:
            decryption()
        elif user_input == 3:
            is_using = False
        else:
            print(f"{user_input} is an INVALID option!")

if __name__ == "__main__":
    main()
