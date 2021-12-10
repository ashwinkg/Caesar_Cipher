from art import logo
print(logo)

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(input_text,shift_amount,cipher_direction):
    output_text=""
    if cipher_direction == "encode":
        for letter in input_text:
            if letter not in alphabet:
                output_text+=letter
            else:
                output_text+=alphabet[((alphabet.index(letter)+shift_amount)%26)]
        
    
    elif cipher_direction =="decode":
        for letter in input_text:
            if letter not in alphabet:
                output_text+=letter
            else:
                output_text+=alphabet[(alphabet.index(letter)-shift_amount)]
    print(f"The {cipher_direction}d text is {output_text}")

end_program=False
while not end_program:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    caesar(input_text=text,shift_amount=shift,cipher_direction=direction)
    user_input=input("Enter 'yes' to continue or 'no' to stop: \n").lower()
    if user_input=="no":
        end_program=True
        print("GoodBye\n")
    print("\n")