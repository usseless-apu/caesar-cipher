alphabet= [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',' ',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n',
            'n','o','p','q','r','s','t','u','v','w','x','y','z',' ', 
]
from logo import Art
print(Art)

def ceasar(path, shift, text):
    if path == 'decode' :
        shift = shift*-1

    last_text =" "
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            last_text += alphabet[new_position]
        else:
            last_text += char
    
    print(f"Here The {path}d result: {last_text}")

    
        
should_condition = True
while should_condition:
    path = input("Type 'encode' To Encrypt \n Type 'decode' To Decrypt\n").lower()
    text = input("Enter Your Text ").lower()
    shift = int(input("Enter Your Shifting Number "))
    shift = shift%26
    ceasar(path, shift, text)

    action=input("Type 'Anything Or Yes' To continue Otherwise Type 'no' To Exit \n").lower()
    if action=='no':
        should_condition = False
        print("Goodbye, ta-ta, see you soon!")


