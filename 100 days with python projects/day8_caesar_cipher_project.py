logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(input_text, shift_amount, cipher_direction):
    final_result = ""
    approved_list = [' ', ',', '.', '/', '?', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', ';', "'", '"']
    new_index = 0
    for letter in input_text:
        if letter not in alphabet:
            final_result += letter
        else:
            get_index = alphabet.index(letter)
            if cipher_direction == 'encode':
                new_index = get_index + shift_amount
            elif cipher_direction == 'decode':
                new_index = get_index - shift_amount
            new_letter = alphabet[new_index]
            final_result += new_letter
    print(f"The {cipher_direction}d text: {final_result}")

should_continue = True
while True:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction == 'encode' or direction == 'decode':
            break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)

    result = str(input("Type 'Yes' to continue the program. Otherwise, type 'No' to stop the program.\n")).lower()
    if result == 'no':
        should_continue = False
        print('Goodbye, see you again soon')
        break









                

