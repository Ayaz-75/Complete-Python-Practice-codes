alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x","y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x","y", "z"]

should_continue=True
while should_continue:
    directions=input("Type 'encode' to encrypt and 'decode' to decrypt \n")
    text = input("Enter your message\n").lower()
    shift=int(input("Type shift number\n"))
    shift=shift%26

    def caesar(start_text,shift_amount,cipher_direction):
        end_text=" "
        if cipher_direction=="decode":
                shift_amount*=-1
        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_amount
                end_text +=alphabet[new_position]
            else:
                end_text+=char
        print(f"The {cipher_direction}d text is {end_text}")
    caesar(start_text=text,shift_amount=shift,cipher_direction=directions)


    result=input("type yes to rerun and no to end: \n")
    if result=="no":
        should_continue=False
        print("Goodbye")
