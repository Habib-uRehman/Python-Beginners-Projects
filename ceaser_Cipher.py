# Ceaser Cipher Project.
# first create a ftn of encrypt, then ftn of decrypt, then message of direction, then create one ftn and embed both ftn in one called ceaser

def ceaser(text, shift, direction):
    for t in text:
        if t.isalpha():

            if direction == 'decode':
                index = alphabets.index(t) - shift
            elif direction == 'encode':
                index = alphabets.index(t) + shift
            else:
                print("enter Correct spelling of Encode OR Decode")
            text = text.replace(t, alphabets[index])
    print(f"The Encoded Text is {text}")


# #THE REASON I PUT A-Z TWO TIMES IS BECAUSE THERE IS NO INDACIES AFTER 25 (Z) SO WHEN I ENTER ZULU INDEX OF Z
# BECOMES 30, # BY ADDING TWO TIMES IT IS NOW BACK TO A

alphabets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(
    ' ')
ask = 'no'
while ask != 'yes':
    direction = input("Type Encode to encrypt, Type Decode to Decrypt \n").lower()
    text = input("Type Your Message. \n").lower()
    shift = int(input("Enter Shift Number\n"))
    shift = shift % 26  # this will allow us to put any shift number. like 1333
    ceaser(text=text, shift=shift, direction=direction)
    leave = input("Do you want to leave the program 'yes' Or 'No'\n")
    ask = leave

# Testing For Special Symbols and numbers. so the num and symbols remains the same.

text = input("Enter your Text")  # Such as text ='oggvogcv3'

shift = int(input("Enter Shift Number"))  # such as shift = 2

for t in text:
    if t.isalpha() == True:
        index = alphabets.index(t) - shift
        text = text.replace(t, alphabets[index])
print(f"The Encoded Text is {text}")
